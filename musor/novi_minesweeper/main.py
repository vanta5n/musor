import tkinter as tk
from cells import *
import draw as draw
from random import shuffle
from options import *


cell_width = WIDTH // N
cell_height = HEIGHT // M

cells = []
open_cells = 0
mines = BOMBS

lost = False

def start():
    global open_cells, lost
    open_cells = 0
    lost = False
    cells.clear()
    for x in range(N):
        cells.append([Cell(x * cell_width, y * cell_height) for y in range(M)])
    for x in range(N):
        for y in range(M):
            draw.cell(cells[x][y], canvas)
    draw.mine_counter(BOMBS, canvas)

def set_bombs(x0, y0):
    global mines
    bomb_places = [(x, y) for x in range(N) for y in range(M)]
    shuffle(bomb_places)
    mines = 0
    for i in range(len(bomb_places)):
        if BOMBS == mines:
            break
        x, y = bomb_places[i]
        dist_to_start = abs(x0 - x) + abs(y0 - y)
        if dist_to_start <= 1 or abs(x0 - x) == abs(y0 - y) == 1:
            continue
        cells[x][y].is_bomb = True
        mines += 1
        for (x1, y1) in [(x - 1, y - 1), (x, y - 1), (x + 1, y - 1),
                         (x - 1, y), (x + 1, y),
                         (x - 1, y + 1), (x, y + 1), (x + 1, y + 1)]:
            if 0 <= x1 < N and 0 <= y1 < M:
                cells[x1][y1].number += 1
    draw.mine_counter(mines, canvas)

def lose():
    global lost
    print('you lost!')
    for x in range(N):
        for y in range(M):
            if cells[x][y].is_bomb and not cells[x][y].is_marked:
                draw.mine(x, y, canvas)
            elif cells[x][y].is_marked and not cells[x][y].is_bomb:
                draw.cross(x, y, canvas)
    lost = True

def open_cell(x, y, active=True):
    global open_cells, mines
    if cells[x][y].is_open and not active:
        return
    if cells[x][y].is_open:
        countflags = 0
        for (x1, y1) in [(x - 1, y - 1), (x, y - 1), (x + 1, y - 1),
                         (x - 1, y),                 (x + 1, y),
                         (x - 1, y + 1), (x, y + 1), (x + 1, y + 1)]:
            if 0 <= x1 < N and 0 <= y1 < M:
                countflags += cells[x1][y1].is_marked
        if countflags >= cells[x][y].number:
            for (x1, y1) in [(x - 1, y - 1), (x, y - 1), (x + 1, y - 1),
                             (x - 1, y), (x + 1, y),
                             (x - 1, y + 1), (x, y + 1), (x + 1, y + 1)]:
                if 0 <= x1 < N and 0 <= y1 < M and not cells[x1][y1].is_marked and not cells[x1][y1].is_open:
                    open_cell(x1, y1, active=False)
        return

    try:
        cells[x][y].open()
    except LoseException:
        if not lost:
            lose()
        return

    open_cells += 1
    if open_cells == N * M - BOMBS:
        print("yipee!")
    draw.cell(cells[x][y], canvas)

    if cells[x][y].number == 0:
        for (x1, y1) in [(x - 1, y - 1), (x, y - 1), (x + 1, y - 1),
                         (x - 1, y),                 (x + 1, y),
                         (x - 1, y + 1), (x, y + 1), (x + 1, y + 1)]:
            if 0 <= x1 < N and 0 <= y1 < M and not cells[x1][y1].is_marked:
                open_cell(x1, y1, active=False)


if __name__ == "__main__":

    root = tk.Tk()
    root.title("sweep sweep sweep")
    canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT+50)

    def M1click(event):
        if event.y > HEIGHT:
            if event.x < 100:
                start()
            return
        if lost:
            return
        if open_cells == 0:
            set_bombs(event.x // cell_width, event.y // cell_height)
        open_cell(event.x // cell_width, event.y // cell_height)

    def M2click(event):
        global mines
        x, y = event.x // cell_width, event.y // cell_height
        if cells[x][y].is_open or mines == 0 and not cells[x][y].is_marked:
            return
        cells[x][y].mark()
        draw.cell(cells[x][y], canvas)
        # if cells[x][y].is_marked:
        #     mines -= 1
        # else:
        #     mines += 1
        mines += 1 - 2 * cells[x][y].is_marked
        draw.mine_counter(mines, canvas)

    start()
    draw.button(canvas)
    canvas.bind("<Button-1>", M1click)
    canvas.bind("<Button-3>", M2click)
    canvas.pack()

    root.mainloop()
