import random


size = int(input('size >>> '))
mines = int(input('mine count >>> '))


# for random mine placement

class RandomGen:

    def __init__(self, n):
        self.iterations = 0
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.iterations < self.n:
            self.iterations += 1
            return random.randint(0, size - 1), random.randint(0, size - 1)
        else:
            raise StopIteration


# cell class

class Item:

    def __init__(self, pos: tuple, is_mine=False, is_open=False):
        self.x = pos[0]
        self.y = pos[1]
        self.is_mine = is_mine
        self.is_open = is_open
        self.is_flag = False
        self.n = 0

    def __str__(self):
        if self.is_flag:
            return '\033[7m\033[1m[+]\033[0m'
        if not self.is_open:
            return '[ ]'
        if not self.n:
            return '[0]'
        if self.n == 1:
            return "\033[34m[1]\033[0m"
        if self.n == 2:
            return "\033[32m[2]\033[0m"
        if self.n == 3:
            return "\033[31m[3]\033[0m"
        if self.n == 4:
            return "\033[36m[4]\033[0m"
        if self.n == 5:
            return "\033[33m[5]\033[0m"
        if self.n == 6:
            return "\033[34m[6]\033[0m"
        if self.n == 7:
            return "\033[35m[7]\033[0m"
        return "\033[35m[8]\033[0m"

    def get_n(self):
        if self.n:
            return
        x = self.x
        y = self.y
        positions = [(x + 1, y), (x + 1, y + 1), (x, y + 1), (x - 1, y + 1),
                     (x - 1, y), (x - 1, y - 1), (x, y - 1), (x + 1, y - 1)]
        positions = filter(lambda p: 0 <= p[0] < size and 0 <= p[1] < size, positions)
        for a, b in positions:
            if field[a][b].is_mine:
                self.n += 1

    def open(self):
        if self.is_open:
            return

        if self.is_flag:
            return

        self.is_open = True

        if self.is_mine:
            raise Exception('you blew up!')

        self.get_n()

        if self.n:
            self.is_open = True
            return

        x = self.x
        y = self.y
        positions = [(x + 1, y), (x + 1, y + 1), (x, y + 1), (x - 1, y + 1),
                     (x - 1, y), (x - 1, y - 1), (x, y - 1), (x + 1, y - 1)]
        positions = filter(lambda p: 0 <= p[0] < size and 0 <= p[1] < size, positions)
        for a, b in positions:
            field[a][b].open()

    def flag(self):
        self.is_flag = not self.is_flag


# generating random field

field = []

for i in range(size):
    field.append([])
    for j in range(size):
        field[i].append(Item((i, j)))

gen = RandomGen(mines)
for x, y in gen:
    if field[x][y].is_mine:
        gen.iterations -= 1
        continue
    field[x][y].is_mine = True

# game itself

while any([not i.is_mine and not i.is_open for j in field for i in j]):

    print('/  ' + '   '.join(str(aaa) for aaa in range(size)))
    for q in range(size):
        print(q, *field[q])

    inpt = input('>>> ').split()
    oa, ob = int(inpt[1]), int(inpt[2])

    if inpt[0].lower() == 'f':
        field[oa][ob].flag()
        continue

    field[oa][ob].open()


print('/  ' + '   '.join(str(aaa) for aaa in range(size)))
for q in range(size):
    print(q, *field[q])

print('\n\033[32m\033[1mSuccess!!\033[0m')
