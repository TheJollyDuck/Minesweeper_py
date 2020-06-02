"""
 Shaun Recto
 The Jolly Duck

 Created: 24/05/20
 Last Modified: 02/06/20

 Minesweeper Console Functions
 This py file contains the necessary functions of the game in console mode
 You may look and/or modify the code as you wish without harming it
 """

import tkinter_functions as tk
import random as r

def gameInitialize():
    print("=====| Welcome to Minesweeper! |=====\n\nPlease type what version you would like to play:")
    version = input("[console]/[GUI]: ")
    version.lower()

    versionSet = False
    while not versionSet:
        if version == "console":
            versionSet = True
            return 1

        elif version == "gui":
            versionSet = True
            return 2

        else:
            print("Please type a valid option")
            version = input("[console]/[GUI]: ")

def boardInitialize():
    mineBoard = []
    hiddenBoard = []
    for i in range(0,10):
        mineBoard.append([])
        hiddenBoard.append([])
        for j in range(0,10):
            mineBoard[i].append("•")
            hiddenBoard.append("•")

    return (mineBoard, hiddenBoard)

def printBoard(mapList):
    yLength = len(mapList)
    for i in range(yLength):
        for j in range(yLength):
            print(mapList[i][j], end ="  ")
            if j == (yLength-1):
                print("")

def placeMines(mapList, quant):
    bomb = "💣"

    for i in range(0,quant):
        xCoord = r.randint(len(mapList))
        yCoord = r.randint(len(mapList[1]))

        if mapList[xCoord, yCoord] == bomb:
            i -= 1
        else:
            mapList[xCoord, yCoord] = bomb
