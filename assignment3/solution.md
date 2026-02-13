## Exercise 1

### 1. 

The unobserved variable X_t represents the weather state at time t. It can take two values:
- Rain (R): It is raining at time t
- No Rain (NR): It is not raining at time t

### 2.

The observable variable E_t represents whether an umbrella is observed at time t. It can take two values:
- Umbrella (U): An umbrella is carried/observed
- No Umbrella (NU): No umbrella is carried/observed

### 3.

#### Dynamic Model P(X_t | X_{t-1})

The transition matrix A, where rows are X_{t-1} and columns are X_t:

| X_{t-1} \ X_t | Rain (R) | No Rain (NR) |
|----------------|----------|--------------|
| Rain (R)      | 0.7      | 0.3          |
| No Rain (NR)  | 0.3      | 0.7          |

#### Observation Model P(E_t | X_t)

The Observation matrix B, where rows are X_t and columns are E_t:

| X_t \ E_t | Umbrella (U) | No Umbrella (NU) |
|-----------|---------------|------------------|
| Rain (R)  | 0.9           | 0.1              |
| No Rain (NR) | 0.2         | 0.8              |

### 4. 

The model assumes a discrete-time framework with time slices (0, 1, 2, ...) where the interval Δ between slices is constant. Each slice contains the same set of variables: unobservable state variables X_t and observable evidence variables E_t. In the umbrella world, X_t represents whether it is raining (Rain_t), and E_t represents whether an umbrella is observed (Umbrella_t). The state sequence starts at t=0, with evidence from t=1 onward.

These assumptions are reasonable as they model temporal processes discretely, allowing probabilistic inference about hidden weather states from umbrella observations over time.
