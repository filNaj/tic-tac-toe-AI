import tkinter as tk
import random

board = [
    [0 for _ in range(3)] for _ in range(3)
]  # output [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


def insert_letter(row, column):
    global player

    if space_is_free(row, column) and not is_winner():
        if player == 'X':
            board[row][column]['text'] = 'X'

            if is_winner() is True:
                label.config(text='You Won!')
            elif is_winner() == 'Tie':
                label.config(text='Tie!')
            else:
                player = 'O'
                label.config(text='O Turn ')
                disable_buttons()
                window.after(1000, computer_move)
                window.after(1000, enable_buttons)

        else:
            board[row][column]['text'] = 'O'

            if is_winner() is True:
                label.config(text='O Won :( ')
            elif is_winner() == 'Tie':
                label.config(text='Tie!')
            else:
                player = 'X'
                label.config(text='X Turn ')


def space_is_free(row, column):
    return board[row][column]['text'] == ''


def is_winner():
    # Check rows
    for row in board:
        if row[0]['text'] == row[1]['text'] == row[2]['text'] != '':
            return True

    # Check columns
    for col in range(3):
        if (
            board[0][col]['text']
            == board[1][col]['text']
            == board[2][col]['text']
            != ''
        ):
            return True

    # Check diagonals
    if board[0][0]['text'] == board[1][1]['text'] == board[2][2]['text'] != '':
        return True
    if board[0][2]['text'] == board[1][1]['text'] == board[2][0]['text'] != '':
        return True

    # Check for a Tie
    if board_is_full():
        return 'Tie'

    return False


def select_random(li):
    ln = len(li)
    r = random.randrange(0, ln)
    return li[r]


def computer_move():
    # Possible winning move
    for letter in ['O', 'X']:
        for move in possible_moves():
            row = move[0]
            col = move[1]
            board[row][col]['text'] = letter
            if is_winner():
                board[row][col]['text'] = ''
                insert_letter(row, col)
                return row, col
            board[row][col]['text'] = ''

    # Corners
    corners = []
    for move in possible_moves():
        if move in [[0, 0], [0, 2], [2, 0], [2, 2]]:
            corners.append(move)
    if len(corners) > 0:
        corner = select_random(corners)
        row = corner[0]
        col = corner[1]
        insert_letter(row, col)
        return row, col

    # Center
    if [1, 1] in possible_moves():
        insert_letter(1, 1)
        return 1, 1

    # Edges
    edges = []
    for move in possible_moves():
        if move in [[0, 1], [1, 0], [1, 2], [2, 1]]:
            edges.append(move)
    if len(edges) > 0:
        edge = select_random(edges)
        row = edge[0]
        col = edge[1]
        insert_letter(row, col)
        return row, col


def possible_moves():
    available_positions_indices = []
    for row in range(len(board)):
        for col in range(len(board[0])):
            if space_is_free(row, col):
                position = [row, col]
                available_positions_indices.append(position)
    return available_positions_indices


def board_is_full():
    spaces = 9
    for row in board:
        for element in row:
            if element['text'] != '':
                spaces -= 1

    if spaces == 0:
        return True
    else:
        return False


def new_game():
    global player
    player = random.choice(players)
    label.config(text=player + ' Turn')

    if player == 'O':
        disable_buttons()
        window.after(1000, computer_move)
        window.after(1000, enable_buttons)

    for row in board:
        for col in row:
            col['text'] = ''


def disable_buttons():
    for row in board:
        for button in row:
            button.config(state=tk.DISABLED, disabledforeground=button['foreground'])


def enable_buttons():
    for row in board:
        for button in row:
            button.config(state=tk.NORMAL)


# Tkinter
window = tk.Tk()
window.title('Tic Tac Toe')

players = ['X', 'O']
player = random.choice(players)

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

if player == 'O':
    disable_buttons()
    window.after(1000, computer_move)
    window.after(1000, enable_buttons)

window.mainloop()
