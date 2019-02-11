# *************************************************************************** #
# 
# Name
# 	ofc_solver - provide optimal solutions for open face chinese poker
# 
# Synopsis
# 	python3 ofc_solver.py
#	python3 ofc_solver.py [NUM PLAYERS]
#
# Author
#	Matthew Kuang
#
# *************************************************************************** #

import sys
from players import print_all_boards

CONST_VERSION = 1.0

print('\x1b[0;31;40m' + 'Open Face Chinese Poker Solver\n' + '\x1b[0m')
print('\x1b[0;34;40m' + 'Version ' + str(CONST_VERSION) + '\x1b[0m')
print('\x1b[0;34;40m' + 'This program was developed by Matthew Kuang\n' 
	+ '\x1b[0m')

num_players = 0
if len(sys.argv) == 2:
	num_players = sys.argv[1]
else:
	valid = False
	while(not valid):
		number = input('\x1b[0;32;40m' + 'Enter the number of players (2-4): ' + 
			'\x1b[0m')
		try:
			num_players = int(number)
		except ValueError:
			print(str(number) + ' is not a valid integer')
		else:
			if num_players >= 2 and num_players <= 4:
				valid = 1

input('\x1b[0;32;40m' + 
	'Would you like to (1) random deal or (2) input cards? ' + '\x1b[0m')

print_all_boards(num_players)
