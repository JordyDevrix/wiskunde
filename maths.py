import math


def steekproef_verdeling(p: float, n: int):
    n = math.sqrt(n)
    return float(p / n)


def standaard_afwijking(p: float, n: int):
    p = p * (1 - p)
    x = float(p / n)
    return float(math.sqrt(x))

