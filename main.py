"""
 Shaun Recto
 The Jolly Duck

 Created: 24/05/20
 Last Modified: 01/06/20

 Minesweeper
 This py file deals with all the necessary logic for the game
 It's also dependent on the py files contained in the same folder
"""

import console_functions as cf
import tkinter_functions as tkf

print("\n============================")
print("Minesweeper is starting.....")
print("============================\n")

gameMode = cf.gameInitialize()
playAgain = True

while playAgain:
    if gameMode == 1:

        mineBoard, hiddenBoard = cf.boardInitialize()
        gameState = "incomplete"
        while gameState == "incomplete":
            cf.printBoard(mineBoard) # for the board the player will look at
            print("")
            cf.printBoard(hiddenBoard) # the hidden board that contains the location of the mines
            print("")
            mineBoard, gameState = cf.chooseMove(mineBoard, hiddenBoard, gameState)
        againQuestion = input("Do you want to play again?\n[yes][no]: ")

        if againQuestion == "yes":
            continue
        else:
            print("Thanks for playing!")
            playAgain = False

End = input("Press [Enter] to exit out of program")