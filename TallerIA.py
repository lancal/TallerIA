import main


def menu():

    print("Welcome to Nim Game\n")

    print("\n")
    print("****************************\n")
    print("      Welcome to Menu       \n")
    print("   Please choose a Option   \n")
    print("****************************\n")
    print("  1) MinMax                 \n")
    print("  2) Tree alpha-bea         \n")
    print("  3) Exit                   \n")

    print("Rules:\n"
          "1) There are 15 sticks in 3 arrows.(See image)\n")

    print("****************************\n")


def menuOption():

    menu()

    option = input("Option: ")

    print ("\n")

    return option


def optionValidated(option):

    if(option != "1" and option != "2" and option != "3"):

        print("Please, give a Valid Option\n")

        option2 = menuOption

        return option2

    if(option == "1" or option == "2"  or option == "3"):

        return option


def startGame():
    flag = True

    while flag != False:

        option = menuOption()

        optionValidate = optionValidated(option)

        if optionValidate == "1":

            #main.Tablero().Mostrar()

            game = main.Game(15, "H")

            main.main_play(game)

            root = main.Node(game.initial)

            newroot = main.makeTreeMinimax(root,game)

            #main.representTree(newroot, game)

        if optionValidate == "2":

            game = main.Game(15,"H")

            main.main_play(game)

            root = main.Node(game.initial)

            newroot = main.makeTreeAplhaBeta(root,game)



        if optionValidate == "3":
            flag = False


if __name__ == '__main__':

    startGame()
