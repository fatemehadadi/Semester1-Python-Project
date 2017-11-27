import os
import game as quoridor

def _show_menu(pm):
	os.system('clear')
	print('*** %s ***'%(pm))
	print('1.quoridor')
	print('2.battleship')
	print('3.exit')

def _is_valid(cmd):
	return cmd in ['1','2','3']

def _execute(cmd):
	if cmd=='1':
		return quoridor.init()
	else cmd=='3':
		exit()

def init():
	pm='Hi! Please choose a number :) '
	while True :
		_show_menu(pm)
		cmd=input('Choise:')
		if _is_valid(cmd):
			pm=_execute(cmd)

		
