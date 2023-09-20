import requests as r
import json
import sys


def main():

    if len(sys.argv) != 2:
        sys.exit("Sólo admite un argumento")

    try:
        n_bc = float(sys.argv[1].replace(",", "."))
    except ValueError:
        sys.exit("No se ingresó un número")

    precio = obtener_precio()
    print(f"${precio * n_bc :,.4f}")


def obtener_precio():
    api = r.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
    return api["bpi"]["USD"]["rate_float"]


if __name__ == "__main__":
    main()
