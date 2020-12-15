
import random

def flip_coin():
    rand_int = random.randrange(1,100)
    if rand_int % 2:
        print ("Heads")
    else:
        print("Tails")


def main():
    flip_coin()

main()


