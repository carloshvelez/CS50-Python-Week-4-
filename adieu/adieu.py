import inflect
p = inflect.engine()

def main():

    nombres = []
    while True:
        try:
            nombre = input("Name: ")
            nombres.append(nombre)
        except(EOFError):
            generar_texto(nombres)
            break



def generar_texto(lista):
    print("Adieu, adieu, to", p.join(lista))







if __name__ == "__main__":
    main()