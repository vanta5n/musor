class LoseException(Exception):
    pass

class Cell:
    def __init__(self, x: int, y: int, bomb: bool = False):
        self.x = x
        self.y = y
        self.is_bomb = bomb
        self.is_open = False
        self.is_marked = False
        self.number = 0

    def mark(self):
        self.is_marked = not self.is_marked

    def open(self):
        if self.is_marked or self.is_open:
            return
        if self.is_bomb:
            raise LoseException('бум')
        self.is_open = True
