import random
import sys


def main():
    nivel = get_level()
    contador_problemas = 0
    contador_errores = 0
    puntos = 0

    while contador_problemas < 10:
        x = generate_integer(nivel)
        y = generate_integer(nivel)

        try:
            respuesta = int(input(f"{x} + {y} = "))
            if respuesta == x + y:
                puntos += 1
                contador_problemas += 1
                continue

            if respuesta != x + y:
                contador_problemas += 1
                print("EEE")

                for i in range(2):
                    respuesta = int(input(f"{x} + {y} = "))
                    if respuesta != x + y:
                        print("EEE")
                    else:
                        puntos += 1
                        break
                print(f"{x} + {y} = {x + y}")

            continue

        except (ValueError):
            contador_errores += 1
            contador_problemas += 1
            print("EEE")
            pass

    print(f"Score: {puntos}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level < 1 or level > 3:
                raise ValueError
            return level

        except (ValueError):
            pass


def generate_integer(level):

    try:
        match level:
            case 1:
                return random.randint(0, 9)
            case 2:
                return random.randint(10, 99)
            case 3:
                return random.randint(100, 999)

    except ValueError:
        sys.exit()


if __name__ == "__main__":
    main()
