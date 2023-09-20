import random
import sys

def main():
    while True:
        try:
            nivel = int(input("Level: "))

            if nivel > 0:
                break
        except(ValueError):
            pass

    correcto = random.randint(1, nivel)

    guess = 150

    while guess != correcto:
        try:
            guess = int(input("Guess: "))
            if guess < 1:
                continue
            elif guess < correcto:
                print("Too small!")
            elif guess > correcto:
                print("Too large!")
        except(ValueError):
            pass

    sys.exit("Just right!")



main()


