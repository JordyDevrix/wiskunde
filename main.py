import maths


def main():
    p = maths.steekproef_proportie(deel=146, geheel=470)
    antwoord = maths.betrouwbaarheidsinterval_95(p=p, sigma=maths.standaard_afwijking(p, 470), _format=True)
    print(antwoord)


if __name__ == '__main__':
    main()
