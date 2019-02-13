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
from input_handler import *

CONST_VERSION = 1.0

print('\x1b[0;31;40m' + 'Open Face Chinese Poker Solver\n' + '\x1b[0m')
print('\x1b[0;34;40m' + 'Version ' + str(CONST_VERSION) + '\x1b[0m')
print('\x1b[0;34;40m' + 'This program was developed by Matthew Kuang\n' 
	+ '\x1b[0m')

num_players = 0	# 2-4 Players
game_mode = 0	# 1 - Random deal (simulation), 2 - Custom input
game_over = False

# Get the number of players
if len(sys.argv) == 2:
	num_players = sys.argv[1]
else:
	num_players = input_num_players()

print_all_boards(num_players)

# Request game mode from user
game_mode = input_mode()

# Options
while(not game_over):
	opt = input_options()
	if opt.upper() == 'Q':
		game_over = True

