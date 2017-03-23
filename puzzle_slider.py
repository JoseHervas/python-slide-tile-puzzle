# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 11:00:19 2017

@author: jhervas
"""

import pandas, os, msvcrt

BOARDWIDTH = 3  # number of columns in the board
BOARDHEIGHT = 3 # number of rows in the board
BLANK = None
CORRECT_DASHBOARD = '1.0  2.0  3.0\n4.0  5.0  6.0\n7.0  8.0  NaN'

def getStartingBoard():
    counter = 1
    board = []
    for x in range(BOARDWIDTH):
        column = []
        for y in range(BOARDHEIGHT):
            column.append(counter)
            counter += BOARDWIDTH
        board.append(column)
        counter -= BOARDWIDTH * (BOARDHEIGHT - 1) + BOARDWIDTH - 1

    board[BOARDWIDTH-1][BOARDHEIGHT-1] = BLANK
    
    board = pandas.DataFrame(board)
    return board
         
def slide(board, blank_position, direction):
    if (direction == "Up"):
        value_above_blank = board[blank_position[0]][blank_position[1]-1]
        board.set_value(blank_position[1], blank_position[0], value_above_blank)
        board.set_value(blank_position[1]-1, blank_position[0], BLANK)
        new_blank_position = [blank_position[0], blank_position[1]-1]
        return new_blank_position
    if (direction == "Down"):
        value_below_blank = board[blank_position[0]][blank_position[1]+1]
        board.set_value(blank_position[1], blank_position[0], value_below_blank)
        board.set_value(blank_position[1]+1, blank_position[0], BLANK)
        new_blank_position = [blank_position[0], blank_position[1]+1]
        return new_blank_position
    if (direction == "Left"):
        value_left_blank = board[blank_position[0]-1][blank_position[1]]
        board.set_value(blank_position[1], blank_position[0], value_left_blank)
        board.set_value(blank_position[1], blank_position[0]-1, BLANK)
        new_blank_position = [blank_position[0]-1, blank_position[1]]
        return new_blank_position
    if (direction == "Right"):
        value_right_blank = board[blank_position[0]+1][blank_position[1]]
        board.set_value(blank_position[1], blank_position[0], value_right_blank)
        board.set_value(blank_position[1], blank_position[0]+1, BLANK)
        new_blank_position = [blank_position[0]+1, blank_position[1]]
        return new_blank_position

def printBoard(board):
    printable_board = board.fillna("_")
    print(printable_board.to_string(index=False, header=False, float_format=lambda x:str(int(x))))

def keyboard_input(): 
   x = msvcrt.kbhit()
   if x: 
        ret = ord(msvcrt.getch()) 
        if ret == 80:
            return "Down"
        elif ret == 72:
            return "Up"
        elif ret == 75:
            return "Left"
        elif ret == 77:
            return "Right"

board = getStartingBoard()
new_blank_position = [BOARDWIDTH-1,BOARDHEIGHT-1]
os.system('cls')
print("\n\n")
print('Welcome to the Slide Puzzle!!!!')
print('Use the arrows on your keyboard to move the blank space')
print('\n')
printBoard(board)
while (board.to_string(index=False, header=False) != CORRECT_DASHBOARD):
    movement = keyboard_input()
    if movement != None:
        new_blank_position = slide(board, new_blank_position, movement)
        os.system('cls')
        print("\n\n")
        print('Welcome to the Slide Puzzle!!!!')
        print('Use the arrows on your keyboard to move the blank space')
        print('\n')
        printBoard(board)
    

    

