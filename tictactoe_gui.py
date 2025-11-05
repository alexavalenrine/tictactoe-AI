import tkinter as tk
from tkinter import messagebox
import math

def check_winner(board):
    # Rows, columns, diagonals
    for row in board:
        if row[0] == row[1] == row[2] != "":
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != "":
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] != "":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != "":
        return board[0][2]
    return None

def is_full(board):
    return all(cell != "" for row in board for cell in row)

def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner == "O":
        return 1
    elif winner == "X":
        return -1
    elif is_full(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == "":
                    board[i][j] = "O"
                    score = minimax(board, depth + 1, False)
                    board[i][j] = ""
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == "":
                    board[i][j] = "X"
                    score = minimax(board, depth + 1, True)
                    board[i][j] = ""
                    best_score = min(score, best_score)
        return best_score

def ai_move():
    best_score = -math.inf
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == "":
                board[i][j] = "O"
                score = minimax(board, 0, False)
                board[i][j] = ""
                if score > best_score:
                    best_score = score
                    move = (i, j)
    if move:
        board[move[0]][move[1]] = "O"
        buttons[move[0]][move[1]].config(text="O", state="disabled")
        check_game_over()

def check_game_over():
    winner = check_winner(board)
    if winner:
        messagebox.showinfo("Game Over", f"{winner} wins!")
        reset_board()
    elif is_full(board):
        messagebox.showinfo("Game Over", "It's a draw!")
        reset_board()

def on_click(row, col):
    if board[row][col] == "":
        board[row][col] = "X"
        buttons[row][col].config(text="X", state="disabled")
        if not check_winner(board) and not is_full(board):
            ai_move()
        check_game_over()

def reset_board():
    global board
    board = [["" for _ in range(3)] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text="", state="normal")

# Window setup
root = tk.Tk()
root.title("Tic Tac Toe AI")

board = [["" for _ in range(3)] for _ in range(3)]
buttons = [[None for _ in range(3)] for _ in range(3)]

for i in range(3):
    for j in range(3):
        button = tk.Button(root, text="", font=("Arial", 24), width=5, height=2,
                           command=lambda r=i, c=j: on_click(r, c))
        button.grid(row=i, column=j)
        buttons[i][j] = button

root.mainloop()
