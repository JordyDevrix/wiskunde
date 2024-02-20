import math


def steekproef_verdeling(sigma: float, n: int) -> float:
    n = math.sqrt(n)
    return float(sigma / n)


def standaard_afwijking(p: float, n: int) -> float:
    p = p * (1 - p)
    x = float(p / n)
    return float(math.sqrt(x))


def steekprf_btrwbaarheidinterval_95(x: float, s: float, n: float, _format: bool = False) -> float or str:
    antwoord = {}
    n = math.sqrt(n)
    tssn_antwrd = 2 * (s / n)
    antwoord[0] = float(x - tssn_antwrd)
    antwoord[1] = float(x + tssn_antwrd)
    if not _format:
        return antwoord
    else:
        return f"[{antwoord[0]:.3f};{antwoord[1]:.3f}]"


def steekproef_proportie(deel: float, geheel: float) -> float:
    return float(deel / geheel)


def betrouwbaarheidsinterval_95(p: float, sigma: float, _format: bool = False) -> str or float:
    antwoord = {}
    waarde_een = p - (2 * sigma)
    waarde_twee = p + (2 * sigma)
    antwoord[0] = waarde_een
    antwoord[1] = waarde_twee
    if not _format:
        return antwoord
    else:
        return f"[{antwoord[0]:.3f};{antwoord[1]:.3f}]"