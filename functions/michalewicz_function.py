import numpy as np
def MICHALEWICS(X):
    """
    Michalewicz benchmark function D-dimension
    https://www.sfu.ca/~ssurjano/michal.html
    """
    DIM = len(X)
    SUM = 0
    M = 10
    for I_COUNT in range(DIM):
        X_I = X[I_COUNT]
        SUM += np.sin(X_I) * (np.sin((I_COUNT * X_I ** 2) / np.pi)**(2 * M))
    Y = - SUM
    return Y