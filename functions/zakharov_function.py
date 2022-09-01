def ZAKHAROV(X):
    """
    Zakharov benchmark function D-dimension
    https://www.sfu.ca/~ssurjano/zakharov.html
    """
    DIM = len(X)
    SUM_1 = 0
    SUM_2 = 0
    for I_COUNT in range(DIM):
        X_I = X[I_COUNT]
        SUM_1 += X_I ** 2
        SUM_2 += (0.5 * I_COUNT * X_I)
    Y = SUM_1 + SUM_2**2 + SUM_2**4
    return Y