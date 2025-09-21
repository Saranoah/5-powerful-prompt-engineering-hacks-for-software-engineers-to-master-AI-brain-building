# Practical Neural Network Model Prompts

## 1. Constraint Optimization Prompt
**Objective**: Transform system limitations into optimization parameters
```
Given current model constraints [memory, compute, latency], generate an optimization strategy that:
- Identifies bottlenecks as feature engineering opportunities
- Converts limitations into regularization terms
- Outputs a configuration that maximizes performance within bounds
- Returns implementation steps with measurable metrics
```

## 2. System Access Pattern Analysis
**Objective**: Analyze and optimize data access patterns
```
Analyze the provided system architecture and:
- Map all data flow pathways and access points
- Identify permission hierarchies and their computational costs
- Generate efficient query patterns that minimize overhead
- Output pseudocode for optimized data retrieval functions
- Include security considerations and access validation steps
```

## 3. Anomaly Detection in Unstructured Data
**Objective**: Identify patterns in noisy or incomplete datasets
```
Process the input data stream and:
- Implement noise filtering algorithms suitable for real-time processing
- Develop pattern recognition for edge cases and outliers
- Create adaptive thresholds that learn from data distribution changes
- Output structured analysis with confidence intervals
- Provide actionable insights for system improvement
```

## 4. Minimal Viable Architecture Design
**Objective**: Design efficient, minimal system architectures
```
Design a system architecture that:
- Achieves maximum functionality with minimal components
- Handles expected load with graceful degradation patterns
- Implements proper error handling and recovery mechanisms
- Uses clear, maintainable code structures
- Includes monitoring and logging capabilities
```

## 5. Iterative Model Improvement Framework
**Objective**: Create self-improving model systems
```
Implement a continuous improvement loop that:
- Monitors model performance against defined KPIs
- Automatically triggers retraining when drift is detected
- Maintains version control and rollback capabilities
- Implements A/B testing for model updates
- Generates performance reports with optimization recommendations
- Ensures system stability throughout the improvement cycle
```

## Implementation Guidelines

### For each prompt:
1. **Define clear success metrics** - What does "working" look like?
2. **Specify input/output formats** - Ensure reproducible results
3. **Include error handling** - Plan for edge cases and failures
4. **Add logging/monitoring** - Track performance and issues
5. **Document assumptions** - Make implicit requirements explicit

### Technical Considerations:
- **Scalability**: Design for growth in data volume and user load
- **Maintainability**: Write code that others can understand and modify
- **Security**: Implement proper authentication and data protection
- **Performance**: Optimize for the specific use case requirements
- **Testing**: Include unit tests and integration test strategies
