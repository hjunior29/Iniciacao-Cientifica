import numpy as np
def GRIEWANK(X):
    """
    Griewank benchmark function D-dimension
    https://www.sfu.ca/~ssurjano/griewank.html
    """
    DIM = len(X)
    SUM = 0
    for I_COUNT in range(DIM):
        X_I = X[I_COUNT]
        SUM += (X_I ** 2) / 4000
    PROD = np.cos(X_I / np.sqrt(X_I))
    Y = SUM - PROD + 1
    return Y