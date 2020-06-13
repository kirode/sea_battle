from ships import Desc, Board, Ship


desc = Desc(3)
ship1 = Ship(desc)
ship2 = Ship(desc)

ships = [ship1, ship2]

print('game begins')
desc.print_desc()

while not all(ship.destroyed for ship in ships):
    user_input_x = int(input('type X coordinate for attack: '))
    user_input_y = int(input('type Y coordinate for attack: '))
    miss = True
    for ship in ships:
        for board in ship.boards:
            if (user_input_x, user_input_y) == (board.x_coordinate, board.y_coordinate):
                board.destroyed = True
                miss = False
                break
        if all(board.destroyed for board in ship.boards):
            ship.destroyed = True
        if ship.destroyed:
            ships.remove(ship)
            print('ship destroyed, good job!')
    if not miss:
        desc.desc[user_input_x][user_input_y] = 'X'
        print('board knocked down, nice!')
    else:
        desc.desc[user_input_x][user_input_y] = '.'
        print('sorry, u missed')
    desc.print_desc()

if all(ship.destroyed for ship in ships):
    print('congratulations, you win the game!')
