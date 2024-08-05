import tkinter as tk
import random


class SliderPuzzle:
    def __init__(self, master):
        self.master = master
        self.master.title("Slider Puzzle")

        self.grid_size = 4
        self.tiles = list(range(1, self.grid_size * self.grid_size))
        self.tiles.append(None)
        self.buttons = []

        self.frame = tk.Frame(self.master)
        self.frame.pack()

        self.create_buttons()
        self.shuffle_tiles()
        self.update_buttons()

        self.master.bind("<Key>", self.handle_key_press)

    def create_buttons(self):
        for i in range(self.grid_size):
            row = []
            for j in range(self.grid_size):
                button = tk.Button(self.frame, width=4, height=2)
                button.grid(row=i, column=j)
                row.append(button)
            self.buttons.append(row)

    def shuffle_tiles(self):
        random.shuffle(self.tiles)
        while not self.is_solvable() or self.is_solved():
            random.shuffle(self.tiles)

    def update_buttons(self):
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                tile = self.tiles[i * self.grid_size + j]
                button = self.buttons[i][j]
                if tile is None:
                    button.config(text="", state=tk.DISABLED)
                else:
                    button.config(text=str(tile), state=tk.NORMAL)

    def handle_key_press(self, event):
        empty_index = self.tiles.index(None)
        empty_row, empty_col = divmod(empty_index, self.grid_size)

        if event.keysym == "Up" and empty_row < self.grid_size - 1:
            self.swap_tiles(empty_index, empty_index + self.grid_size)
        elif event.keysym == "Down" and empty_row > 0:
            self.swap_tiles(empty_index, empty_index - self.grid_size)
        elif event.keysym == "Left" and empty_col < self.grid_size - 1:
            self.swap_tiles(empty_index, empty_index + 1)
        elif event.keysym == "Right" and empty_col > 0:
            self.swap_tiles(empty_index, empty_index - 1)

        self.update_buttons()
        if self.is_solved():
            self.display_win_message()

    def swap_tiles(self, i, j):
        self.tiles[i], self.tiles[j] = self.tiles[j], self.tiles[i]

    def is_solvable(self):
        inv_count = 0
        for i in range(len(self.tiles)):
            for j in range(i + 1, len(self.tiles)):
                if self.tiles[i] and self.tiles[j] and self.tiles[i] > self.tiles[j]:
                    inv_count += 1
        return inv_count % 2 == 0

    def is_solved(self):
        return self.tiles == list(range(1, self.grid_size * self.grid_size)) + [None]

    def display_win_message(self):
        win_label = tk.Label(self.master, text="You Win!", font=("Arial", 24))
        win_label.pack()


if __name__ == "__main__":
    root = tk.Tk()
    game = SliderPuzzle(root)
    root.mainloop()
