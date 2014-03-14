# TEMP file: for testing ONLY

from checkers_board import *
from printer import *
from assets import *
from helpers import *
from movement import *


# Print empty wooden board
b = CheckersBoard(piece)
print_board(b.wooden_board)

# Set and print initial board
b.set_pieces_on_board_for_a_new_game(initial_white_positions, initial_black_positions)
print_board(b.wooden_board)

# Check if the board returns the correct piece
print b.get_piece([7, 0])

m = Movement(b, piece)

#  position parser shouldn't be a part of movement class. Movement class should deal with rows and columns only
init_pos = position_parser('c3')
fin_pos = position_parser('b4')

# Make and check a simple move
m.make_simple_move(init_pos, fin_pos)
print_board(b.wooden_board)


# Make and check a capturing nove
b.set_piece([4, 5], 'b')
print_board(b.wooden_board)
m.make_capture_move([5, 4], [3, 6])
print_board(b.wooden_board)


# Yet to decide where to place this method