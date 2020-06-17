"""
 Shaun Recto
 The Jolly Duck

 Created: 24/05/20
 Last Modified: 17/06/2020

 Minesweeper Console Functions
 This py file contains the necessary functions of the game in console mode
 You may look and/or modify the code as you wish without harming it
 """

# import tkinter_functions as tk
import random as r
import string as st

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
    xLength = len(mapList[1])
    CAPITAL_LIST = st.ascii_uppercase
    LOWERCASE_LIST = st.ascii_lowercase
    ALPHABET_SIZE = 26

    print(" \t", end = "")
    for i in range(xLength):
        if i < 26:
            print(CAPITAL_LIST[i], "\t", end = "")
        else:
            print(LOWERCASE_LIST[i - ALPHABET_SIZE], "\t", end = "")
    print("")

    for i in range(yLength):
        line = ""
        print(i, end = "\t")
        for j in range(xLength):
            line += mapList[i][j] + "{}".format("\t")
            if j == (xLength-1):
                print(line)

def difficulty():
    def easy():
        rs = 9
        cs = 9
        ms = 10
        return rs, cs, ms

    def medium():
        rs = 16
        cs = 16
        ms = 40
        return rs, cs, ms

    def hard():
        rs = 16
        cs = 30
        ms = 99
        return rs, cs, ms

    def custom():
        rs = customLevel("rows")
        cs = customLevel("columns")
        ms = customLevel("mines")
        return rs, cs, ms

    difDict = {
        "easy" : easy,
        "medium" : medium,
        "hard" : hard,
        "custom" : custom
    }

    difChosen = False

    while not difChosen:
        dif = input("What difficulty you want to play on?\n [easy][medium][hard][custom]: ")
        dif.lower()
        if dif in difDict:
            rows, columns, mines = difDict.get(dif)()
            difChosen = True
        else:
            print("\n===[Invalid Response]===")

    return rows, columns, mines

def placeMines(mapList, quant):
    bomb = "\U0001F4A3"
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

def placeNumbers(mapList):
    ...

def checkIfInt(var):
    while not var.isdigit():
        var = input("That is not a valid response. Try again: ")
    var = int(var)
    return var

def customLevel(word):
    number = checkIfInt(input("Please type the number of {} you want: ".format(word)))
    return number