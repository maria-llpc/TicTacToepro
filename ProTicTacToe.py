import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root, username):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.username = username
        self.current_player = "X"  # Initialize with "X"
        self.create_widgets()

    def create_widgets(self):
        self.label_username = tk.Label(self.root, text=f"Welcome, {self.username}!")
        self.label_username.pack()

        self.button_start = tk.Button(self.root, text="Start Game", command=self.start_game)
        self.button_start.pack()

    def start_game(self):
        self.root.destroy()
        game_window = tk.Tk()
        game_window.title("Tic Tac Toe Game")

        buttons = [[None, None, None], [None, None, None], [None, None, None]]

        def check_winner():
            for row in buttons:
                if row.count(row[0]) == 3 and row[0] is not None:
                    return row[0]

            for col in range(3):
                if buttons[0][col] == buttons[1][col] == buttons[2][col] and buttons[0][col] is not None:
                    return buttons[0][col]

            if buttons[0][0] == buttons[1][1] == buttons[2][2] and buttons[0][0] is not None:
                return buttons[0][0]

            if buttons[0][2] == buttons[1][1] == buttons[2][0] and buttons[0][2] is not None:
                return buttons[0][2]

            return None

        def button_click(row, col):
            if buttons[row][col] is None:
                buttons[row][col] = self.current_player

                button = tk.Button(game_window, text=buttons[row][col], font=('normal', 20), width=6, height=2,
                                   command=lambda r=row, c=col: button_click(r, c))
                button.grid(row=row, column=col)

                winner = check_winner()
                if winner:
                    messagebox.showinfo("Game Over", f"Player {winner} wins!")
                    game_window.destroy()
                elif all(button is not None for row in buttons for button in row):
                    messagebox.showinfo("Game Over", "It's a tie!")
                    game_window.destroy()

                # Switch player after each move
                self.current_player = "O" if self.current_player == "X" else "X"

        for i in range(3):
            for j in range(3):
                button = tk.Button(game_window, text="", font=('normal', 20), width=6, height=2,
                                   command=lambda r=i, c=j: button_click(r, c))
                button.grid(row=i, column=j)
                buttons[i][j] = None

if __name__ == "__main__":
    root = tk.Tk()

    def validate_login():
        username = entry_username.get()
        password = entry_password.get()
        if username and password:
            app = TicTacToe(root, username)
        else:
            messagebox.showerror("Error", "Invalid username or password")

    root.title("Login")
    root.geometry("300x150")

    label_username = tk.Label(root, text="Username:")
    label_username.pack()

    entry_username = tk.Entry(root)
    entry_username.pack()

    label_password = tk.Label(root, text="Password:")
    label_password.pack()

    entry_password = tk.Entry(root, show="*")
    entry_password.pack()

    button_login = tk.Button(root, text="Login", command=validate_login)
    button_login.pack()

    root.mainloop()
