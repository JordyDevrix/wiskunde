import maths


def main():
    p = maths.steekproef_proportie(deel=146, geheel=470)
    antwoord = maths.betrouwbaarheidsinterval_95(p=p, sigma=maths.standaard_afwijking(p, 470), _format=True)
    print(antwoord)
    print(maths.steekprf_btrwbaarheidinterval_95(x=700, s=40, n=24, _format=True))
    print(maths.remweg(_snelheid=50))
    print(maths.reactie_afstand(_snelheid=50))
    print(
        f"totale stop afstand: "
        f"{maths.stop_afstand(_reactie_afstand=maths.remweg(_snelheid=50), _remweg=maths.reactie_afstand(_snelheid=50))}"
    )


if __name__ == '__main__':
    main()
