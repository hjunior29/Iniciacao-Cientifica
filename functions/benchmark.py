# $$\      $$\ $$$$$$$$\ $$$$$$$$\  $$$$$$\        $$$$$$$$\  $$$$$$\   $$$$$$\  $$\       $$$$$$$\   $$$$$$\  $$\   $$\
# $$$\    $$$ |$$  _____|\__$$  __|$$  __$$\       \__$$  __|$$  __$$\ $$  __$$\ $$ |      $$  __$$\ $$  __$$\ $$ |  $$ |
# $$$$\  $$$$ |$$ |         $$ |   $$ /  $$ |         $$ |   $$ /  $$ |$$ /  $$ |$$ |      $$ |  $$ |$$ /  $$ |\$$\ $$  |
# $$\$$\$$ $$ |$$$$$\       $$ |   $$$$$$$$ |         $$ |   $$ |  $$ |$$ |  $$ |$$ |      $$$$$$$\ |$$ |  $$ | \$$$$  /
# $$ \$$$  $$ |$$  __|      $$ |   $$  __$$ |         $$ |   $$ |  $$ |$$ |  $$ |$$ |      $$  __$$\ $$ |  $$ | $$  $$<
# $$ |\$  /$$ |$$ |         $$ |   $$ |  $$ |         $$ |   $$ |  $$ |$$ |  $$ |$$ |      $$ |  $$ |$$ |  $$ |$$  /\$$\
# $$ | \_/ $$ |$$$$$$$$\    $$ |   $$ |  $$ |         $$ |    $$$$$$  | $$$$$$  |$$$$$$$$\ $$$$$$$  | $$$$$$  |$$ /  $$ |
# \__|     \__|\________|   \__|   \__|  \__|         \__|    \______/  \______/ \________|\_______/  \______/ \__|  \__|

################################################################################
# UNIVERSIDADE FEDERAL DE CATALÃO (UFCAT)
# WANDERLEI MALAQUIAS PEREIRA JUNIOR,                  ENG. CIVIL / PROF (UFCAT)
# JOÃO V. COELHO ESTRELA,                                     ENG. MINAS (UFCAT)
################################################################################

################################################################################
# DESCRIÇÃO ALGORITMO:
# BIBLIO. META DE FUNÇÕES DE BENCHMARK DESENVOLVIDA PELO GRUPO DE PESQUISA E
# ESTUDOS EM ENGENHARIA (GPEE)
################################################################################

################################################################################
# BIBLIOTECAS NATIVAS PYTHON
import numpy as np
import random

# FUNÇÃO SPHERE
def SPHERE(X):
    """
    Sphere benchmark function D-dimension
    """
    DIM = len(X)
    SUM = 0
    for I_COUNT in range(DIM):
        X_I = X[I_COUNT]
        SUM += X_I ** 2
    Y = SUM
    return Y

# FUNÇÃO ROSENBROCK
def ROSENBROCK(X):
    """
    Rosenbrock benchmark function D-dimension
    """
    DIM = len(X)
    SUM = 0
    for I_COUNT in range(DIM - 1):
        X_I = X[I_COUNT]
        X_NEXT = X[I_COUNT + 1]
        NEW = 100 * (X_NEXT - X_I ** 2) ** 2 + (X_I - 1) ** 2
        SUM += NEW
    Y = SUM
    return Y

# FUNÇÃO RASTRIGIN
def RASTRIGIN(X):
    """
    Rastrigin benchmark function D-dimension
    """
    DIM = len(X)
    SUM = 0
    for I_COUNT in range(DIM):
        X_I = X[I_COUNT]
        SUM += (X_I ** 2 - 10 * np.cos(2 * np.pi * X_I))
    Y = 10 * DIM + SUM
    return Y

# FUNÇÃO ACKLEY
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

# FUNÇÃO GRIEWANK
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

# FUNÇÃO ZAKHAROV
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

# FUNÇÃO EASOM
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

# FUNÇÃO MICHALEWICS
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

class HILL_CLIMBING:

    def randomSolution(tsp):
        cities = list(range(len(tsp)))
        solution = []

        for i in range(len(tsp)):
            randomCity = cities[random.randint(0, len(cities) - 1)]
            solution.append(randomCity)
            cities.remove(randomCity)

        return solution

    def routeLength(tsp, solution):
        routeLength = 0
        for i in range(len(solution)):
            routeLength += tsp[solution[i - 1]][solution[i]]
        return routeLength

    def getNeighbours(solution):
        neighbours = []
        for i in range(len(solution)):
            for j in range(i + 1, len(solution)):
                neighbour = solution.copy()
                neighbour[i] = solution[j]
                neighbour[j] = solution[i]
                neighbours.append(neighbour)
        return neighbours

    def getBestNeighbour(tsp, neighbours):
        bestRouteLength = routeLength(tsp, neighbours[0])
        bestNeighbour = neighbours[0]
        for neighbour in neighbours:
            currentRouteLength = routeLength(tsp, neighbour)
            if currentRouteLength < bestRouteLength:
                bestRouteLength = currentRouteLength
                bestNeighbour = neighbour
        return bestNeighbour, bestRouteLength

    def hillClimbing(tsp):
        currentSolution = randomSolution(tsp)
        currentRouteLength = routeLength(tsp, currentSolution)
        neighbours = getNeighbours(currentSolution)
        bestNeighbour, bestNeighbourRouteLength = getBestNeighbour(tsp, neighbours)

        while bestNeighbourRouteLength < currentRouteLength:
            currentSolution = bestNeighbour
            currentRouteLength = bestNeighbourRouteLength
            neighbours = getNeighbours(currentSolution)
            bestNeighbour, bestNeighbourRouteLength = getBestNeighbour(tsp, neighbours)

        return currentSolution, currentRouteLength

    def main():
        tsp = [
            [0, 400, 500, 300],
            [400, 0, 300, 500],
            [500, 300, 0, 400],
            [300, 500, 400, 0]
        ]

        print(hillClimbing(tsp))

    if __name__ == "__main__":
        main()

#   /$$$$$$  /$$$$$$$  /$$$$$$$$ /$$$$$$$$       /$$$$$$$$ /$$$$$$$$  /$$$$$$  /$$   /$$ /$$   /$$  /$$$$$$  /$$        /$$$$$$   /$$$$$$  /$$$$$$ /$$$$$$$$  /$$$$$$
#  /$$__  $$| $$__  $$| $$_____/| $$_____/      |__  $$__/| $$_____/ /$$__  $$| $$  | $$| $$$ | $$ /$$__  $$| $$       /$$__  $$ /$$__  $$|_  $$_/| $$_____/ /$$__  $$
# | $$  \__/| $$  \ $$| $$      | $$               | $$   | $$      | $$  \__/| $$  | $$| $$$$| $$| $$  \ $$| $$      | $$  \ $$| $$  \__/  | $$  | $$      | $$  \__/
# | $$ /$$$$| $$$$$$$/| $$$$$   | $$$$$            | $$   | $$$$$   | $$      | $$$$$$$$| $$ $$ $$| $$  | $$| $$      | $$  | $$| $$ /$$$$  | $$  | $$$$$   |  $$$$$$
# | $$|_  $$| $$____/ | $$__/   | $$__/            | $$   | $$__/   | $$      | $$__  $$| $$  $$$$| $$  | $$| $$      | $$  | $$| $$|_  $$  | $$  | $$__/    \____  $$
# | $$  \ $$| $$      | $$      | $$               | $$   | $$      | $$    $$| $$  | $$| $$\  $$$| $$  | $$| $$      | $$  | $$| $$  \ $$  | $$  | $$       /$$  \ $$
# |  $$$$$$/| $$      | $$$$$$$$| $$$$$$$$         | $$   | $$$$$$$$|  $$$$$$/| $$  | $$| $$ \  $$|  $$$$$$/| $$$$$$$$|  $$$$$$/|  $$$$$$/ /$$$$$$| $$$$$$$$|  $$$$$$/
#  \______/ |__/      |________/|________/         |__/   |________/ \______/ |__/  |__/|__/  \__/ \______/ |________/ \______/  \______/ |______/|________/ \______/