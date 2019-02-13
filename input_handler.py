# Script for handling input for the Open Face Chinese Poker Solver

def generic_input(message, type):
	valid = False
	while(not valid):
		inp = input('\x1b[0;32;40m' + message + 
			'\x1b[0m')
		try:
			result = int(inp)
		except ValueError:
			print('\x1b[0;31;40m' + str(inp) + ' is not a valid option')
		else:
			if type == 'num_players':
				if result >= 2 and result <= 4:
					valid = 1
				else:
					print('\x1b[0;31;40m' + 'Please enter a number 2-4')
			elif type == 'mode':
				if result == 1 or result == 2:
					valid = 1
					result = 1	# Change later
				else:
					print('\x1b[0;31;40m' + 'Please enter a number 1-2')
	return result

def input_num_players():
	return generic_input('Enter the number of players (2-4): ', 'num_players')

def input_mode():
	return generic_input(
			'Would you like to  use the (1) solver or (2) simulator? ', 'mode')

def input_options():
	print('\x1b[0;32;40m' + 'Please select an option:')
	print('(1) Random deal 3 cards')
	print('(2) Choose 3 cards')
	print('(3) Set your board (Player 1)')
	print('(4) Set another board')
	print('(Q) Quit' + '\x1b[0m')
	opt = input()
	return str(opt)
