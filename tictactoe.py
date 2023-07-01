import tkinter as tk
import random


def insertLetter(row, column):
    global player
    if player == 'X':
        if board[row][column]['text'] == '' and not isWinner():
            board[row][column]['text'] = 'X'

            if not isWinner():
                player = 'O'
                label.config(text='O Turn ')

            elif isWinner():
                label.config(text='You Won!')

            elif isWinner() == 'Tie':
                label.config(text='Tie!')


def spaceIsFree(pos):
    pass


def isWinner():
    pass


def playerMove():
    pass


def selectRandom(li):
    pass


def computerMove():
    pass


def isBoardFull(board):
    pass


def new_game():
    pass


def main():
    pass


# Tkinter
window = tk.Tk()
window.title('Tic Tac Toe')

players = ['X', 'O']
player = random.choice(players)
board = [
    [0 for _ in range(3)] for _ in range(3)
]  # output [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

label = tk.Label(text=player + ' Turn')
label.pack(side='top')

restart_btn = tk.Button(text='Restart', command=new_game)
restart_btn.pack(side='top')

frame = tk.Frame(window)
frame.pack(side='top')

# Create grid
for row in range(3):
    for column in range(3):
        board[row][column] = tk.Button(
            frame,
            width=10,
            height=5,
            command=lambda row=row, col=column: insertLetter(row, col),
        )
        board[row][column].grid(row=row, column=column)

window.mainloop()
