import numpy as np

# Exercise 2: HMM Filtering using Forward Algorithm

# States: 0 = Rain, 1 = No Rain
# Transition matrix T (P(X_t | X_{t-1}))
T = np.array([[0.7, 0.3], [0.3, 0.7]])

# Initial prior P(X_0)
prior = np.array([0.5, 0.5])

def get_observation_matrix(umbrella_present):
    """
    Returns the observation matrix O_t for the given evidence.
    umbrella_present: True if umbrella observed, False otherwise.
    """
    if umbrella_present:
        # P(E_t | X_t): Rain -> 0.9, No Rain -> 0.2
        return np.array([[0.9, 0], [0, 0.2]])
    else:
        # P(E_t | X_t): Rain -> 0.1, No Rain -> 0.8
        return np.array([[0.1, 0], [0, 0.8]])

def forward_step(f_prev, O, T):
    """
    Computes the next forward message: f_{1:t+1} = α O_{t+1} T^T f_{1:t}
    Returns the normalized forward message.
    """
    # Unnormalized forward message
    unnorm = O @ T.T @ f_prev
    # Normalization constant α
    alpha = 1 / np.sum(unnorm)
    # Normalized
    return alpha * unnorm

# Part 1: Verify with P(X_2 | e_{1:2}) where e1=e2=True (umbrella both days)
print("Verification: P(X_2 | umbrella on day 1 and 2)")
evidence_verify = [True, True]  # e1, e2
f = prior.copy()
for i, e in enumerate(evidence_verify, start=1):
    O = get_observation_matrix(e)
    f = forward_step(f, O, T)
    print(f"Normalized f_1:{i} = {f}")

print(f"P(Rain at day 2) = {f[0]:.3f}")

print("\n" + "="*50 + "\n")

# Part 2: Calculate P(X_5 | e_{1:5}) for the given sequence
print("Sequence: e_{1:5} = {Umbrella1=True, Umbrella2=True, Umbrella3=False, Umbrella4=True, Umbrella5=True}")
evidence_full = [True, True, False, True, True]  # e1 to e5
f = prior.copy()
for i, e in enumerate(evidence_full, start=1):
    O = get_observation_matrix(e)
    f = forward_step(f, O, T)
    print(f"Normalized f_1:{i} = {f}")

print(f"\nFinal P(Rain at day 5) = {f[0]:.3f}")

