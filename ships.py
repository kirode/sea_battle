from random import choice


class Desc:
    def __init__(self, size):
        self.size = size
        self.desc = []
        self.ships = []
        self.free_cells = [(a, b) for a in range(0, self.size) for b in range(0, self.size)]
        for row in range(self.size):
            self.desc.append(['O'] * self.size)

    def print_desc(self):
        for item in self.desc:
            print(item)


class Board:
    def __init__(self, x, y):
        self.x_coordinate = x
        self.y_coordinate = y
        self.destroyed = False


class Ship:
    size = 1

    def __init__(self, desc):
        self.boards = []
        for board in range(self.size):
            self.boards.append(self.generate_board(desc))
        self.destroyed = False

    def generate_board(self, desc):
        if len(self.boards) == 0:
            coordinates = choice(desc.free_cells)
            a, b = coordinates
            delete_coordinates = [(x, y) for x in range(a-1, a+2) for y in range(b-1, b+2)]
            for item in delete_coordinates:
                if item in desc.free_cells:
                    desc.free_cells.remove(item)
            return Board(a, b)


if __name__ == '__main__':
    desc = Desc(10)
    ship1 = Ship(desc)
    desc.print_desc()
    print(ship1.boards[0].__dict__)
    print(desc.free_cells)
