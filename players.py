p1_t = "xx xx xx"		# Player 1's top board
p1_m = "xx xx xx xx xx"	# Player 1's middle board
p1_b = "xx xx xx xx xx"	# Player 1's bottom board

p2_t = "xx xx xx"
p2_m = "xx xx xx xx xx"
p2_b = "xx xx xx xx xx"

p3_t = "xx xx xx"
p3_m = "xx xx xx xx xx"
p3_b = "xx xx xx xx xx"

p4_t = "xx xx xx"
p4_m = "xx xx xx xx xx"
p4_b = "xx xx xx xx xx"

board = [p1_t, p1_m, p1_b, p2_t, p2_m, p2_b, p3_t, p3_m, p3_b, p4_t, p4_m, p4_b]

def print_all_boards(num_players):
	for i in range(0, num_players):
		print_board(i)

def print_board(player):
	n = int(player*3)
	# print(board[n] + '\n' + board[n+1] + '\n' + board[n+2])
	actual_p = player + 1
	print('\x1b[0;33;40m' + 'Player ' + str(actual_p) + ':\n' + board[n] + 
		'\n' + board[n+1] + '\n' + board[n+2] + '\n\x1b[0m')

print_all_boards(2)

