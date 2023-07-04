import tkinter as tk
import random


def insert_letter(row, column):
    global player

    if space_is_free(row, column) and not is_winner():
        if player == 'X':
            board[row][column]['text'] = 'X'

            if not is_winner():
                player = 'O'
                label.config(text='O Turn ')
                # computer_move

            elif is_winner():
                label.config(text='You Won!')

            elif is_winner() == 'Tie':
                label.config(text='Tie!')

        else:
            board[row][column]['text'] = 'O'

            if not is_winner():
                player = 'X'
                label.config(text='X Turn ')

            elif is_winner():
                label.config(text='O Won')

            elif is_winner() == 'Tie':
                label.config(text='Tie!')


def space_is_free(row, column):
    return board[row][column]['text'] == ''


def is_winner():
    # Check rows
    for row in board:
        if row[0]['text'] == row[1]['text'] == row[2]['text'] != '':
            return True

    # Check columns
    for col in range(3):
        if (board[0][col]['text'] == board[1][col]['text'] == board[2][col]['text'] != ''):
            return True

    # Check diagonals
    if board[0][0]['text'] == board[1][1]['text'] == board[2][2]['text'] != '':
        return True
    if board[0][2]['text'] == board[1][1]['text'] == board[2][0]['text'] != '':
        return True

    # Check for a Tie
    if not space_is_free():
        return 'Tie'

    return False


def player_move():
    pass


def selectRandom(li):
    pass


def computer_move():
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col]['text'] == '':
                for letter in ['O', 'X']:
                    if not is_winner():
                        boardCopy = [rows[:] for rows in board]
                        boardCopy[row][col]['text'] = letter


def board_is_full(board):
    pass

    for row in board:
        for button in row:
            if button['text'] == '':
                return True
    return False


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
            command=lambda row=row, col=column: insert_letter(row, col),
        )
        board[row][column].grid(row=row, column=column)

window.mainloop()
