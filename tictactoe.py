import tkinter as tk
import random


def insertBoard(letter, pos):
    pass


def spaceIsFree(pos):
    pass


def isWinner(bo, le):
    pass


def playerMove():
    pass


def selectRandom(li):
    pass


def compMove():
    pass


def isBoardFull(board):
    pass


def printBoard():
    pass


def new_game():
    pass


def main():
    pass


window = tk.Tk()
window.title('Tic Tac Toe')
players = ['X', 'O']
player = random.choice(players)
buttons = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

label = tk.Label(text=player + ' Turn')
label.pack(side='top')

restart_btn = tk.Button(text='Restart', command=new_game)
restart_btn.pack(side='top')

frame = tk.Frame(window)
frame.pack(side='top')

for row in range(3):
    for column in range(3):
        buttons[row][column] = tk.Button(frame, width=10, height=5, command='compMove')
        buttons[row][column].grid(row=row, column=column)

window.mainloop()
