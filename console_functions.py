# Shaun Recto
# The Jolly Duck
#
# Created: 24/05/20
# Last Modified: 24/05/20
#
# Minesweeper Console Functions
# This py file contains the necessary functions of the game in console mode
# You may look and/or modify the code as you wish without harming it

def gameInitialize():
    print("Welcome to Minesweeper.\nPlease type what version you would like to play:\n")
    version = input("[console]/[GUI]: ")
    version.lower()

    versionSet = False
    while not version:
        if version == "console":
            versionSet = True
        elif version == "gui":
            versionSet = True
        else:
            print("Please type a valid option")
            version = input("[console]/[GUI]: ")

def boardInitialize():
    ...