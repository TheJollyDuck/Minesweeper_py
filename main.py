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

print("============================")
print("Minesweeper is starting.....")
print("============================\n")

gameMode = cf.gameInitialize()
if gameMode == 1:

    mineBoard, hiddenBoard = cf.boardInitialize()
    cf.printBoard(mineBoard) # for the board the player will look at
    print()
    cf.printBoard(hiddenBoard) # the hidden board that contains the location of the mines

End = input("Press [Enter] to exit out of program")