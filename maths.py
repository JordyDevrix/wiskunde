import math


def steekproef_verdeling(sigma: float, n: int):
    n = math.sqrt(n)
    return float(sigma / n)


def standaard_afwijking(p: float, n: int):
    p = p * (1 - p)
    x = float(p / n)
    return float(math.sqrt(x))


def steekproef_proportie(deel: float, geheel: float):
    return float(deel / geheel)


def betrouwbaarheidsinterval_95(p: float, sigma: float, form: bool = False):
    antwoord = {}
    waarde_een = p - (2 * sigma)
    waarde_twee = p + (2 * sigma)
    antwoord[0] = waarde_een
    antwoord[1] = waarde_twee
    if not form:
        return antwoord
    else:
        return f"[{antwoord[0]:.3f};{antwoord[1]:.3f}]"