import quoridor
import battleship
import os


def _show_menu(pm):
    os.system('cls')
    print('*** %s ***' % (pm))
    print('1.quoridor')
    print('2.battleship')
    print('3.exit')


def _is_valid(cmd):
    return cmd in ['1', '2', '3']


def _execute(cmd):
    if cmd == '1':
        return quoridor.init()
    elif cmd == '2':
        return battleship.init()
    elif cmd == '3':
        exit()


def init():
    pm = 'Hi! Please choose a number :) '
    while True:
        _show_menu(pm)
        cmd = input('Your Choise:')
        if _is_valid(cmd):
            pm = _execute(cmd)
