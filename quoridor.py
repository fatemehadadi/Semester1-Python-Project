import os


def _show_game_map(game_board, gamewall, gameline, turn, wallnum1, wallnum_1):
    os.system('cls')
    output = [' %s player turn :' % ('First' if turn == 1 else 'Second')
        , '  a   b   c   d   e   f   g   h   i '
        , '  __  __  __  __  __  __  __  __  __'
        , '1| %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s |' % (
                  game_board[0][0], gamewall[0][0], game_board[0][1], gamewall[0][1], game_board[0][2], gamewall[0][2]
                  , game_board[0][3], gamewall[0][3], game_board[0][4], gamewall[0][4], game_board[0][5],
                  gamewall[0][5],
                  game_board[0][6], gamewall[0][6], game_board[0][7], gamewall[0][7], game_board[0][8])
        , ' | %s . %s . %s . %s . %s . %s . %s . %s . %s |' % (
                  gameline[0][0], gameline[0][1], gameline[0][2], gameline[0][3], gameline[0][4], gameline[0][5],
                  gameline[0][6], gameline[0][7], gameline[0][8])
        , '2| %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s |' % (
                  game_board[1][0], gamewall[1][0], game_board[1][1], gamewall[1][1], game_board[1][2], gamewall[1][2],
                  game_board[1][3], gamewall[1][3], game_board[1][4], gamewall[1][4], game_board[1][5], gamewall[1][5],
                  game_board[1][6], gamewall[1][6], game_board[1][7], gamewall[1][7], game_board[1][8])
        , ' | %s . %s . %s . %s . %s . %s . %s . %s . %s |' % (
                  gameline[1][0], gameline[1][1], gameline[1][2], gameline[1][3], gameline[1][4], gameline[1][5],
                  gameline[1][6], gameline[1][7], gameline[1][8])
        , '3| %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s |' % (
                  game_board[2][0], gamewall[2][0], game_board[2][1], gamewall[2][1], game_board[2][2], gamewall[2][2],
                  game_board[2][3], gamewall[2][3], game_board[2][4], gamewall[2][4], game_board[2][5], gamewall[2][5],
                  game_board[2][6], gamewall[2][6], game_board[2][7], gamewall[2][7], game_board[2][8])
        , ' | %s . %s . %s . %s . %s . %s . %s . %s . %s |' % (
                  gameline[2][0], gameline[2][1], gameline[2][2], gameline[2][3], gameline[2][4], gameline[2][5],
                  gameline[2][6], gameline[2][7], gameline[2][8])
        , '4| %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s |' % (
                  game_board[3][0], gamewall[3][0], game_board[3][1], gamewall[3][1], game_board[3][2], gamewall[3][2],
                  game_board[3][3], gamewall[3][3], game_board[3][4], gamewall[3][4], game_board[3][5], gamewall[3][5],
                  game_board[3][6], gamewall[3][6], game_board[3][7], gamewall[3][7], game_board[3][8])
        , ' | %s . %s . %s . %s . %s . %s . %s . %s . %s |' % (
                  gameline[3][0], gameline[3][1], gameline[3][2], gameline[3][3], gameline[3][4], gameline[3][5],
                  gameline[3][6], gameline[3][7], gameline[3][8])
        , '5| %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s |' % (
                  game_board[4][0], gamewall[4][0], game_board[4][1], gamewall[4][1], game_board[4][2], gamewall[4][2],
                  game_board[4][3], gamewall[4][3], game_board[4][4], gamewall[4][4], game_board[4][5], gamewall[4][5],
                  game_board[4][6], gamewall[4][6], game_board[4][7], gamewall[4][7], game_board[4][8])
        , ' | %s . %s . %s . %s . %s . %s . %s . %s . %s |' % (
                  gameline[4][0], gameline[4][1], gameline[4][2], gameline[4][3], gameline[4][4], gameline[4][5],
                  gameline[4][6], gameline[4][7], gameline[4][8])
        , '6| %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s |' % (
                  game_board[5][0], gamewall[5][0], game_board[5][1], gamewall[5][1], game_board[5][2], gamewall[5][2],
                  game_board[5][3], gamewall[5][3], game_board[5][4], gamewall[5][4], game_board[5][5], gamewall[5][5],
                  game_board[5][6], gamewall[5][6], game_board[5][7], gamewall[5][7], game_board[5][8])
        , ' | %s . %s . %s . %s . %s . %s . %s . %s . %s |' % (
                  gameline[5][0], gameline[5][1], gameline[5][2], gameline[5][3], gameline[5][4], gameline[5][5],
                  gameline[5][6], gameline[5][7], gameline[5][8])
        , '7| %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s |' % (
                  game_board[6][0], gamewall[6][0], game_board[6][1], gamewall[6][1], game_board[6][2], gamewall[6][2],
                  game_board[6][3], gamewall[6][3], game_board[6][4], gamewall[6][4], game_board[6][5], gamewall[6][5],
                  game_board[6][6], gamewall[6][6], game_board[6][7], gamewall[6][7], game_board[6][8])
        , ' | %s . %s . %s . %s . %s . %s . %s . %s . %s |' % (
                  gameline[6][0], gameline[6][1], gameline[6][2], gameline[6][3], gameline[6][4], gameline[6][5],
                  gameline[6][6], gameline[6][7], gameline[6][8])
        , '8| %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s |' % (
                  game_board[7][0], gamewall[7][0], game_board[7][1], gamewall[7][1], game_board[7][2], gamewall[7][2],
                  game_board[7][3], gamewall[7][3], game_board[7][4], gamewall[7][4], game_board[7][5], gamewall[7][5],
                  game_board[7][6], gamewall[7][6], game_board[7][7], gamewall[7][7], game_board[7][8])
        , ' | %s . %s . %s . %s . %s . %s . %s . %s . %s |' % (
                  gameline[7][0], gameline[7][1], gameline[7][2], gameline[7][3], gameline[7][4], gameline[7][5],
                  gameline[7][6], gameline[7][7], gameline[7][8])
        , '9| %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s |' % (
                  game_board[8][0], gamewall[8][0], game_board[8][1], gamewall[8][1], game_board[8][2], gamewall[8][2],
                  game_board[8][3], gamewall[8][3], game_board[8][4], gamewall[8][4], game_board[8][5], gamewall[8][5],
                  game_board[8][6], gamewall[8][6], game_board[8][7], gamewall[8][7], game_board[8][8])
        , ' | __  __  __  __  __  __  __  __  __|',
              'The number of wall you can use: %d' % (wallnum1 if turn == 1 else wallnum_1)]

    for line in output:
        print(line)


def _index(cmd, i, j):
    return (int(cmd[i]) - 1), (int(ord(cmd[j])) - 97)


def _is_valid(game_board, gameline, gamewall, place1, place_1, turn, cmd, wallnum1, wallnum_1):
    clum = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
    row = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    if cmd == '':
        return False
    if cmd[0] == 'w':
        if len(cmd) != 6 or cmd[1] not in ['h', 'v'] \
                or cmd[2] not in row or cmd[3] not in row \
                or cmd[4] not in clum or cmd[5] not in clum:
            return False
        if turn == 1 and wallnum1 == 0:
            return False
        if turn == -1 and wallnum_1 == 0:
            return False
        x, y = _index(cmd, 2, 4)
        if cmd[1] == 'h':
            if gamewall[x][y] == '|' or gamewall[x + 1][y] == '|':
                return False
            elif game_board[x][y] == '_' and gameline[x][y + 1] == '_':
                return False
        elif cmd[1] == 'v':
            if gameline[x][y + 1] == '_' or gameline[x][y] == '_':
                return False
            elif gamewall[x][y] == '|' and gamewall[x + 1][y] == '|':
                return False
        return True

    elif cmd[0] == 'm':
        if len(cmd) != 3 or cmd[1] not in row or cmd[2] not in clum:
            return False
        x, y = _index(cmd, 1, 2)
        if abs(place1[0] - place_1[0]) == 1 and place1[1] == place_1[1]:
            if gameline[place1[0]][place1[1]] != ' ':
                return False
            if y == place1[1]:
                if place1[0] > place_1[0] and turn == 1 and x == place1[0] - 2:
                    return True
                if place1[0] < place_1[0] and turn == -1 and x == place_1[0] - 2:
                    return True
                if place1[0] > place_1[0] and turn == -1 and x == place_1[0] + 2:
                    return True
                if place1[0] < place_1[0] and turn == 1 and x == place1[0] + 2:
                    return True

        if turn == 1:
            if x != place1[0] and y != place1[1]:
                return False
            if place1[0] == x:
                if abs(place1[1] - y) != 1:
                    return False
                min = place1[1] if place1[1] < y else y
                if gamewall[x][min] != ' ':
                    return False
            if place1[1] == y:
                if abs(place1[0] - x) != 1:
                    return False
                if gameline[place1[0]][place1[1]] == '_':
                    return False
        else:
            if x != place_1[0] and y != place_1[1]:
                return False
            if place_1[0] == x:
                if abs(place_1[1] - y) != 1:
                    return False
                min = place_1[1] if place_1[1] < y else y
                if gamewall[x][min] != ' ':
                    return False
            if place_1[1] == y:
                if abs(place_1[0] - x) != 1:
                    return False
                if gameline[place_1[0] - 1][place_1[1]] != ' ':
                    return False
        return True
    elif cmd[0] == 'q':
        return True
    return False


def _move(game_board, place1, place_1, cmd, turn):
    x, y = _index(cmd, 1, 2)
    game_board[x][y] = '*' if turn == 1 else '0'
    if turn == 1:
        game_board[place1[0]][place1[1]] = ' '
        place1[0], place1[1] = (x), (y)
    else:
        game_board[place_1[0]][place_1[1]] = ' '
        place_1[0], place_1[1] = (x), (y)

    return place1, place_1


def _wall(gamewall, gameline, cmd, turn, wallnum1, wallnum_1):
    x, y = _index(cmd, 2, 4)
    if cmd[1] == 'h':
        gamewall[x][y] = '|'
        gamewall[x + 1][y] = '|'

    else:
        gameline[x][y + 1] = '_'
        gameline[x][y] = '_'

    if turn == 1:
        wallnum1 -= 1

    else:
        wallnum_1 -= 1

    return wallnum1, wallnum_1


def _is_win(game_board):
    for i in range(9):
        if game_board[0][i] == '0':
            return True
        if game_board[8][i] == '*':
            return True
    return False


def init():
    gamewall = []
    gameline = []
    game_board = []
    for i in range(9):
        game_board.append([' '] * 9)
    for i in range(0, 8):
        gameline.append([' '] * 9)
    for i in range(9):
        gamewall.append([' '] * 8)

    game_board[0][4] = '*'
    game_board[8][4] = '0'
    turn = 1
    wallnum1 = 10
    wallnum_1 = 10
    place1 = [0, 4]
    place_1 = [8, 4]
    while True:
        _show_game_map(game_board, gamewall, gameline, turn, wallnum1, wallnum_1)
        cmd = input('Enter move: ').strip()
        if _is_valid(game_board, gameline, gamewall, place1, place_1, turn, cmd, wallnum1, wallnum_1):
            if cmd[0] == 'm':
                place1, place_1 = _move(game_board, place1, place_1, cmd, turn)
            elif cmd[0] == 'w':
                wallnum1, wallnum_1 = _wall(gamewall, gameline, cmd, turn, wallnum1, wallnum_1)
            elif cmd[0] == 'q':
                return ' %s player quited from game ' % ('First' if turn == 1 else 'Second',)
            turn *= -1
        else:
            print('Error!')
            continue
        if _is_win(game_board):
            return '%s player won ' % ('First' if turn == -1 else 'Second',)
