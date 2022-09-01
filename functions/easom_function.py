import numpy as np
def EASOM(X):
    """
    Easom benchmark function D-dimension
    https://www.sfu.ca/~ssurjano/easom.html
    """
    X_1 = X[0]
    X_2 = X[1]
    FACT_1 = - np.cos(X_1) * np.cos(X_2)
    FACT_2 = np.exp(- (X_1 - np.pi) ** 2 - (X_2 - np.pi) ** 2)
    Y = FACT_1 * FACT_2
    return Y