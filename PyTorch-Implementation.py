import torch
import torch.nn as nn
import torch.nn.functional as F
import math

def dark_knowledge_distillation_loss(
    student_logits,  # Student model logits for the batch
    teacher_logits,  # Teacher model logits for the batch
    labels,          # True labels for the batch
    temperature,     # Temperature for softening probabilities
    num_classes,     # Number of classes in the dataset
    mu=0.1           # Weight for uncertainty alignment term
):
    # Compute softened probabilities with temperature
    p_T = F.softmax(teacher_logits / temperature, dim=1)
    p_S = F.softmax(student_logits / temperature, dim=1)
    
    # Compute entropies per example (add epsilon for numerical stability)
    U_T = -torch.sum(p_T * torch.log(p_T + 1e-10), dim=1)  # Teacher entropy
    U_S = -torch.sum(p_S * torch.log(p_S + 1e-10), dim=1)  # Student entropy
    
    # Compute cross-entropy loss per example
    L_CE = F.cross_entropy(student_logits, labels, reduction='none')
    
    # Compute KL divergence loss per example (standard distillation loss)
    log_p_S = F.log_softmax(student_logits / temperature, dim=1)
    KL_loss = F.kl_div(log_p_S, p_T, reduction='none') * (temperature * temperature)
    KL_loss = torch.sum(KL_loss, dim=1)  # Sum over classes to get per-example loss
    
    # Compute weight for distillation based on teacher entropy (vulnerabilities)
    max_entropy = math.log(num_classes)  # Maximum possible entropy (nats)
    weight = 1 - U_T / max_entropy  # Weight for KD: low when teacher is uncertain
    
    # Combine losses per example: CE, weighted KD, and uncertainty alignment
    loss_per_example = (1 - weight) * L_CE + weight * KL_loss + mu * (U_S - U_T)**2
    
    # Average loss over the batch
    loss = torch.mean(loss_per_example)
    
    return loss
