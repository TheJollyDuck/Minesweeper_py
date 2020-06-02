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

def gameInitialize():
    print("=====| Welcome to Minesweeper! |=====\n\nPlease type what version you would like to play:")
    version = input("[console]/[GUI]: ")
    version.lower()

    versionSet = False
    while not version:
        if version == "console":
            versionSet = True
            boardInitialize()

        elif version == "gui":
            versionSet = True

        else:
            print("Please type a valid option")
            version = input("[console]/[GUI]: ")

def boardInitialize():
    ...