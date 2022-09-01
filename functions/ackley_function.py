import numpy as np
def ACKLEY(X):
    """
    Ackley benchmark function D-dimension
    https://www.sfu.ca/~ssurjano/ackley.html
    """
    DIM = len(X)
    SUM1 = 0
    SUM2 = 0
    A = 20
    B = 0.2
    C = 2 * np.pi
    for I_COUNT in range(DIM):
        X_I = X[I_COUNT]
        SUM1 += X_I ** 2
        SUM2 += np.cos(C * X_I)
    TERM_1 = -A * np.exp(-B * np.sqrt(SUM1 / DIM))
    TERM_2 = -np.exp(SUM2 / DIM)
    Y = TERM_1 + TERM_2 + A + np.exp(1)
    return Y