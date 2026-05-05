import tkinter as tk
from options import *


cell_width = WIDTH // N
cell_height = HEIGHT // M

def cell(cell, canvas: tk.Canvas):
    x = cell.x
    y = cell.y

    if cell.is_open:
        canvas.create_rectangle(x, y, x + cell_width, y + cell_height, fill="#DDDDDD", outline="#BABABA", width=2)
        canvas.create_text(x + cell_width // 2, y + cell_height // 2,
                           text=str(cell.number),
                           font=('Alegreya Sans', int(cell_height * 0.6), 'bold'),
                           fill=["#DDDDDD", "#0000DD", "#00BC00", "#FF0000", "#000033", "#550000", "#FF6666", "#FFFFFF", "#000000"][cell.number])
    else:
        canvas.create_rectangle(x, y, x + cell_width, y + cell_height, fill="#C0C0C0", outline="#BABABA", width=2)
        if cell.is_marked:
            canvas.create_text(x + cell_width // 2, y + cell_height // 2,
                           text="🚩",
                           font=('Alegreya Sans', int(cell_height * 0.6), 'bold'),
                           fill="#DD0000")


def mine(x, y, canvas: tk.Canvas):
    canvas.create_oval(x * cell_width + cell_width // 3.5, y * cell_height + cell_height // 3.5,
                       x * cell_width + cell_width * 2.5 // 3.5, y * cell_height + cell_height * 2.5 // 3.5,
                       fill='#000000')
    canvas.create_line(x * cell_width + cell_width // 2, y * cell_height + cell_height // 5,
                       x * cell_width + cell_width // 2, y * cell_height + cell_height * 4 // 5,
                       width=2)
    canvas.create_line(x * cell_width + cell_width // 5, y * cell_height + cell_height // 2,
                       x * cell_width + cell_width * 4 // 5, y * cell_height + cell_height // 2,
                       width=2)
    canvas.create_line(x * cell_width + cell_width * 0.28786, y * cell_height + cell_height * 0.28786,
                       (x + 1) * cell_width - cell_width * 0.28786, (y + 1) * cell_height - cell_height * 0.28786,
                       width=2)
    canvas.create_line((x + 1) * cell_width - cell_width * 0.28786, y * cell_height + cell_height * 0.28786,
                       x * cell_width + cell_width * 0.28786, (y + 1) * cell_height - cell_height * 0.28786,
                       width=2)

def cross(x, y, canvas: tk.Canvas):
    canvas.create_line(x * cell_width, y * cell_height, (x + 1) * cell_width, (y + 1) * cell_height, width=2)
    canvas.create_line(x * cell_width, (y + 1) * cell_height, (x + 1) * cell_width, y * cell_height, width=2)

def mine_counter(mines, canvas):
    canvas.create_rectangle(WIDTH - 10, HEIGHT + 10, WIDTH - 90, HEIGHT + 40, fill="#C0C0C0", outline="#BABABA", width=3)
    canvas.create_text(WIDTH - 50, HEIGHT + 25, text=str(mines), font=('Alegreya Sans', 20, 'bold'), fill="#DD0000")

def button(canvas):
    canvas.create_rectangle(10, HEIGHT + 10, 90, HEIGHT + 40, fill="#C0C0C0", outline="#BABABA", width=3)
    canvas.create_text(50, HEIGHT + 25, text='restart', font=('Alegreya Sans', 15, 'bold'), fill="#777777")
