"""
 Shaun Recto
 The Jolly Duck

 Created: 24/05/20
 Last Modified: 15/06/2020

 Minesweeper Console Functions
 This py file contains the necessary functions of the game in console mode
 You may look and/or modify the code as you wish without harming it
 """

# import tkinter_functions as tk
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
    rows, columns, mines = difficulty()
    mineBoard = []
    hiddenBoard = []

    for i in range(0,rows):
        mineBoard.append([])
        hiddenBoard.append([])

        for j in range(0,columns):
            mineBoard[i].append("•")
            hiddenBoard[i].append("•")

    hiddenBoard = placeMines(hiddenBoard, mines)
    return (mineBoard, hiddenBoard)

def printBoard(mapList):
    yLength = len(mapList)

    for i in range(yLength):
        for j in range(yLength):
            print(mapList[i][j], end ="  ")
            if j == (yLength-1):
                print("")

def difficulty():
    difChosen = False
    difNames = ["easy","medium","hard"]
    rowsList = [9, 16, 16]
    columnsList = [9, 16, 30]
    minesList = [10, 40, 99]

    while not difChosen:
        dif = input("What difficulty you want to play on?\n [easy][medium][hard][custom]: ")
        dif.lower()

        if dif == "custom":
            rows = input("Please type the number of rows you want: ")
            rows = checkIfInt(rows)
            columns = input("Please type the number of columns you want: ")
            columns = checkIfInt(columns)
            mines = input("Please type the number of mines you want: ")
            mines = checkIfInt(mines)
            difChosen = True

        else:
            difIndex = difNames.index(dif)
            rows = rowsList[difIndex]
            columns = columnsList[difIndex]
            mines = minesList[difIndex]
            difChosen = True

    return rows, columns, mines

def placeMines(mapList, quant):
    bomb = "💣"
    rowSize = len(mapList)
    columnSize = len(mapList[1])

    while quant > 0:
        rowCoord = r.randint(0,rowSize -1)
        columnCoord = r.randint(0,columnSize -1)

        if mapList[rowCoord][columnCoord] == bomb:
            continue
        else:
            mapList[rowCoord][columnCoord] = bomb
            quant -= 1

    return mapList

def checkIfInt(var):
    while not var.isdigit():
        var = input("That is not a valid response. Try again: ")
    var = int(var)
    return var