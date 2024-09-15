import os
import numpy as np

# ======================================================== FUNCTION ====================================================

# Function to print layout
def layout():
    os.system("cls")
    print("="*34)
    print(" GAME \t:  TIC TAC TOE\n")
    print("\t" + '='*15)
    for i in range(3):
        if i == 1 or i == 2:
            print('\t| ', '-'*9, ' |') # print line in the middle
        print('\t| ', coloum[i*3+0], '|', coloum[i*3+1], '|', coloum[i*3+2], ' |')
    print("\t" + '='*15, '\n')

# Decide valid or invalid input player 1
def decision_player1(player1):
    if player1 >= 1 and player1 <= 9:
        coloum[(player1 - 1)] = 'X'
    else:
        layout()
        print(" !!  INVALID INPUT PLAYER 1  !!\n")
        return True

# Decide valid or invalid input player 2
def decision_player2(player2):
    if player2 >= 1 and player2 <= 9:
        coloum[(player2 - 1)] = 'O'
    else:
        choice.remove(str(player1))
        coloum[(player1 - 1)] = player1
        layout()
        print(" !!  INVALID INPUT PLAYER 2  !!\n")
        return True

# Check the layout of 'X' or 'O'
def check_layout(value):
    if ((coloum[0] == value) and (coloum[1] == value) and (coloum[2] == value)):
        return True
    elif ((coloum[3] == value) and (coloum[4] == value) and (coloum[5] == value)):
        return True
    elif ((coloum[6] == value) and (coloum[7] == value) and (coloum[8] == value)):
        return True
    elif ((coloum[0] == value) and (coloum[3] == value) and (coloum[6] == value)):
        return True
    elif ((coloum[1] == value) and (coloum[4] == value) and (coloum[7] == value)):
        return True
    elif ((coloum[2] == value) and (coloum[5] == value) and (coloum[8] == value)):
        return True
    elif ((coloum[2] == value) and (coloum[4] == value) and (coloum[6] == value)):
        return True
    elif ((coloum[0] == value) and (coloum[4] == value) and (coloum[8] == value)):
        return True
    else:
        return False

# =================================================== PROGRAM START ====================================================

# Variables
choice = []
coloum = list(range(1,10))

# Print "layout"
layout()

# Game Processing
while True:
# Player 1 Input and Check player 1 input
    player1 = int(input("---> Player X = "))
    if str(player1) in choice:
        layout()
        print(" !!  INVALID INPUT PLAYER 1  !!\n")
        continue
    else:
        if decision_player1(player1):   # Check the input player 1
            continue
        else:
            if check_layout('X'):    # Check the layout of 'X'
                layout()
                print("\tPLAYER 1 WIN !!")
                break
            # if the layout already full
            if len(choice) >= 8:
                layout()
                print("\n  THE GAME ENDED IN A DRAW !!")
                break
        choice += str(player1)
        layout()

# Player 2 Input and Check player 2 input
    while True:
        player2 = int(input("---> Player O = "))
        if str(player2) in choice:
            layout()
            print(" !!  INVALID INPUT PLAYER 2  !!\n")
            continue
        else:
            if decision_player2(player2):   # Check the input player 2
                continue
            choice += str(player2)
            if check_layout('O'):    # Check the layout of 'O'
                layout()
                print("\tPLAYER 2 WIN !!")
                break
            layout()
            break

print("="*34, "\n")
