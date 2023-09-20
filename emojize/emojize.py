import emoji


def main():

    output = input("Input: ")
    print("Output: ", emoji.emojize(output, language="alias"))


if __name__ == "__main__":
    main()
