import random

def Flip_coin():
    randint = random.randrange(0,100)
    if randint % 2:
        print("Heads")
    else:
        print('Tails')

def Display_menu():
    print("Welcome to our shit Discord bot, please enter command from the following. ")
    print("")
    print("To flip a coin type: !flip")
    print("To generate a random team type: !randt")
    print("To generate a random game type: !randg")
    print("To list common games type: !gamesc")
    print("To list your games type: !gamesl")
    print("To add a game to your list type: !gamesa")
    print("To remove a game from your list type !gamesr")
    print("To display menu again type: !menu")
    print()

def Get_user_Command():
    command = input("Please enter desired command. ")
    if command == "!flip":
        Flip_coin()
        print(" ")
        Get_user_Command()

    if command == "!menu":
        Display_menu()
        print(" ")
        Get_user_Command()
            
    if command == "!quit":
        print("Goodbye cunt")


def main():
    Display_menu()
    Get_user_Command()

main()


