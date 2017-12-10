import os


def _show_start_board():
    output = ['    a    b    c    d    e   f    g    h    i    j'
        , '   __   __   __   __   __   __   __   __   __   __  '
        , '1 |                                                |'
        , '2 |                                                |'
        , '3 |                                                |'
        , '4 |                                                |'
        , '5 |                                                |'
        , '6 |                                                |'
        , '7 |                                                |'
        , '8 |                                                |'
        , '9 |                                                |'
        , '10|                                                |'
        , '   __   __   __   __   __   __   __   __   __   __  ']
    for line in output:
        print(line)


def _show_gameboard(game_board1, game_board_1, ship_place1, ship_place_1, turn):
    os.system('cls')

    output1 = ['    a    b    c    d    e   f    g    h    i    j'
        , '   __   __   __   __   __   __   __   __   __   __  ']
    for i in range(10):
        output1.append('%d%s| %s    %s    %s    %s    %s    %s    %s    %s    %s    %s |' % (
            i+1, ' ' if i != 9 else '', game_board_1[i][0], game_board_1[i][1], game_board_1[i][2], game_board_1[i][3]
            , game_board_1[i][4], game_board_1[i][5], game_board_1[i][6], game_board_1[i][7]
            , game_board_1[i][8], game_board_1[i][9]))
    output1.append('   __   __   __   __   __   __   __   __   __   __  ')

    output_1 = ['    a    b    c    d    e   f    g    h    i    j'
        , '   __   __   __   __   __   __   __   __   __   __  ']
    for i in range(10):
        output_1.append('%d%s| %s    %s    %s    %s    %s    %s    %s    %s    %s    %s |' % (
            i+1, ' ' if i != 9 else '', game_board1[i][0], game_board1[i][1], game_board1[i][2], game_board1[i][3]
            , game_board1[i][4], game_board1[i][5], game_board1[i][6], game_board1[i][7]
            , game_board1[i][8], game_board1[i][9],))
    output_1.append('   __   __   __   __   __   __   __   __   __   __  ')

    print(' %s player turn :' % ('First' if turn == 1 else 'Second'))
    print('*Enemy map*                                                             *Your ships*')
    if turn == 1:
        for x in ship_place1:
            if game_board1[x[0]][x[1]] == ' ':
                game_board1[x[0]][x[1]] = 'O'
        for i in range(13):
            print(output1[i], '                    ', output_1[i])
        for x in ship_place1:
            if game_board1[x[0]][x[1]] == 'O':
                game_board1[x[0]][x[1]] = ' '

    else:
        for x in ship_place_1:
            if game_board_1[x[0]][x[1]] == ' ':
                game_board_1[x[0]][x[1]] = 'O'
        for i in range(13):
            print(output_1[i], '                    ', output1[i])
        for x in ship_place_1:
            if game_board_1[x[0]][x[1]] == 'O':
                game_board_1[x[0]][x[1]] = ' '


def _index(string):
    return (int(string[0]) - 1), (int(ord(string[1])) - 97)


def get_ships(ship_place, turn):
    i = 2
    while i != 6:
        first_sit = list(input(
            '%s player please enter the beginning place of 1x%d ship: ' % (
                'First' if turn == 1 else 'Second', i)).strip().split(' '))
        end_sit = list(input(
            '%s player please enter the ending place of 1x%d ship: ' % (
                'First' if turn == 1 else 'Second', i)).strip().split(' '))
        if _is_valid_ship(first_sit, end_sit, ship_place, i):
            x1, y1 = _index(first_sit)
            x2, y2 = _index(end_sit)
            if abs(x1 - x2) == i - 1 and y1 == y2:
                for j in range(i):
                    ship_place.append((x1 + j, y1))
            elif abs(y1 - y2) == i - 1 and x1 == x2:
                for j in range(i):
                    ship_place.append((x1, y1 + j))
        else:
            print('Wrong input!')
            continue
        if i == 3 and len(ship_place) == 5:
            first_sit = list(input(
                '%s player please enter the beginning place of 1x%d ship: ' % (
                    'First' if turn == 1 else 'Second', i)).strip().split(" "))
            end_sit = list(input(
                '%s player please enter the ending place of 1x%d ship: ' % (
                    'First' if turn == 1 else 'Second', i)).strip().split(" "))
            if _is_valid_ship(first_sit, end_sit, ship_place, i):
                x1, y1 = _index(first_sit)
                x2, y2 = _index(end_sit)
                if abs(x1 - x2) == i - 1 and y1 == y2:
                    for j in range(i):
                        ship_place.append((x1 + j, y1))
                elif abs(y1 - y2) == i - 1 and x1 == x2:
                    for j in range(i):
                        ship_place.append((x1, y1 + j))
            else:
                print('Wrong input!')
                continue
        i+=1



def _is_valid_ship(first_sit, end_sit, ship_place, i):
    if len(first_sit) == 2 and first_sit[0] in ['1','2','3','4','5','6','7','8','9','10'] and first_sit[1] in ['a','b','c','d','e','f','g','h','i','j'] \
            and len(end_sit) == 2 and end_sit[0] in ['1','2','3','4','5','6','7','8','9','10'] and end_sit[1] in ['a','b','c','d','e','f','g','h','i','j']:
        print('yes')
        x1, y1 = _index(first_sit)
        x2, y2 = _index(end_sit)
        if abs(x1 - x2) == i - 1 and y1 == y2:
            if x1 > x2:
                x1, x2 = x2, x1
            t = 0
            for j in range(i):
                if (x1 + j, y1) not in ship_place:
                    t += 1
            if t == i:
                return True
        elif abs(y1 - y2) == i - 1 and x1 == x2:
            if y1 > y2:
                y1, y2 = y2, y1
            n = 0
            for j in range(i):
                if (x1, y1 + j) not in ship_place:
                    n += 1
            if n == i:
                return True
    return False


def _is_valid(game_board1, game_board_1, turn, cmd):
    if cmd==('q',):
        return True
    elif len(cmd) == 2 and cmd[0] in ['1','2','3','4','5','6','7','8','9','10'] and cmd[1] in ['a','b','c','d','e','f','g','h','i','j']:
        x,y=_index(cmd)
        if turn ==1 and game_board_1[x][y]==' ':
            return True
        if turn ==-1 and game_board1[x][y]==' ':
            return True
        return False


def hit_ship(cmd, turn, game_board1, game_board_1, ship_place1, ship_place_1):
    if turn == 1:
        x, y = _index(cmd)
        if (x, y) in ship_place_1:
            print('***You hit the ship***')
            game_board_1[x][y] = 'T'
        else:
            print('Your hit was fail...')
            game_board_1[x][y] = 'F'

    else:
        x, y = _index(cmd)
        if (x, y) in ship_place1:
            print('***You hit the ship***')
            game_board1[x][y] = 'T'
        else:
            print('Your hit was fail...')
            game_board1[x][y] = 'F'


def _is_win(game_board1, game_board_1):
    if len([x for x in game_board1 if x == 'T']) == 17 \
            or len([x for x in game_board_1 if x == 'T']) == 17:
        return True
    else:
        return False


def init():
    game_board1 = []
    game_board_1 = []
    ship_place1 = []
    ship_place_1 = []
    for _ in range(10):
        game_board1.append([' '] * 10)
    for _ in range(10):
        game_board_1.append([' '] * 10)
    _show_start_board()
    turn = 1
    get_ships(ship_place_1, turn)
    turn *= -1
    _show_start_board()
    get_ships(ship_place1, turn)
    turn *= -1
    while True:
        _show_gameboard(game_board1, game_board_1, ship_place1, ship_place_1, turn)
        cmd = tuple(input('Enter the place to hit: ').strip().split(" "))
        if cmd == ('q',):
            return '%s player is quited' % ('First' if turn == -1 else 'Second',)
        if _is_valid(game_board1, game_board_1, turn, cmd):
            hit_ship(cmd, turn, game_board1, game_board_1, ship_place1, ship_place_1)
            turn *= -1
        else:
            print('Error!')
            continue
        if _is_win(game_board1, game_board_1):
            return '%s player won ' % ('First' if turn == -1 else 'Second',)
