import sys
import random
from pyfiglet import Figlet

figlet = Figlet()


def main():

    argv = sys.argv

    if len(argv) > 3 or len(argv) == 2:
        sys.exit("Invalid Usage")

    elif len(argv) == 1:
        impresion_aleatoria()

    elif (
        len(argv) == 3
        and (argv[1] == "-f" or argv[1] == "--font")
        and argv[2] in figlet.getFonts()
    ):
        impresion_definida(argv[2])

    else:
        sys.exit("Invalid Usage")


def impresion_aleatoria():
    texto = input("Input: ")
    fuentes = figlet.getFonts()
    figlet.setFont(font=random.choice(fuentes))
    print("Output:", figlet.renderText(texto))


def impresion_definida(fuente):
    texto = input("Input: ")
    figlet.setFont(font=fuente)
    print("Output:", figlet.renderText(texto))


if __name__ == "__main__":
    main()
