import maths


def main():
    p = maths.steekproef_proportie(146, 470)
    antwoord = maths.betrouwbaarheidsinterval_95(p, maths.standaard_afwijking(p, 470))
    print()


if __name__ == '__main__':
    main()
