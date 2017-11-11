import main


def menu():

    print("Welcome to Nim Game\n")
    print("Rules:\n"
          "1) There are 15 sticks in 3 arrows.(See image)\n")


def startGame():

    menu()

    #main.Tablero().Mostrar()

    game = main.Game(15, "H")


    main.main_play(game)

    root = main.Node(game.initial)

    newroot = main.makeTreeMinimax(root,game)

    main.representTree(newroot, game)

    print("asdfasaf")

if __name__ == '__main__':

    startGame()
