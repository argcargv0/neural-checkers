from helpers import *
from assets import *

class MoveList:
    
    def __init__(self, checkers_board, piece):
        self.checkers_board = checkers_board
        self.piece = piece

    def get_move_list(self, position):
        movable_neighbours = self.get_movable_neighbour_cells(position_parser(position))
        move_list = []
        for neighbour in movable_neighbours:
            if self.checkers_board.get_piece(neighbour) == piece['empty']:
                move = position + '-' + readable_position(neighbour)
                move_list.append(move)
        return move_list

    def get_capturing_move_list(self, position):
        self.capture_move_list = []
        [row, column] = position_parser(position)
        piece = self.checkers_board.get_piece([row, column])
        self.get_captures(position, [row, column], piece)
        return self.capture_move_list

    def get_movable_neighbour_cells(self, position):
        [row, column] = position
        piece = self.checkers_board.get_piece(position)
        self.neighbours = []

        # Get neighbours by adding offset. King pieces have two offsets [1, -1]
        for offset in move_offset[piece]:
            self.add_neighbour([row + offset, column + 1])
            self.add_neighbour([row + offset, column - 1])
        
        return self.neighbours

    def add_neighbour(self, neighbour):
        if self.is_valid(neighbour):
            self.neighbours.append(neighbour)

    def is_valid(self, position):
        [row, column] = position
        return 0 <= row <= 7 and 0 <= column <= 7
        
    def get_captures(self, move, position, piece):
        [row, column] = position
        capture_neighbours = self.get_capture_neighbour_cells(position, piece)
        
        for neighbour in capture_neighbours:
            move += "x" + readable_position(neighbour)
            self.get_captures(move, neighbour, piece)

        if capture_neighbours == []:
            self.capture_move_list.append(move)
                
    def get_capture_neighbour_cells(self, position, piece):
        [row, column] = position
        self.capture_neighbours = []

        for offset in move_offset[piece]:
            self.add_capture_neighbour([row, column], [row + offset, column + 1], [row + 2 * offset, column + 2], piece)
            self.add_capture_neighbour([row, column], [row + offset, column - 1], [row + 2 * offset, column - 2], piece)
        
        return self.capture_neighbours

    # TODO: Refactoring
    def add_capture_neighbour(self, initial_position, opponent_position, final_position, piece):
        if self.is_valid(initial_position) and self.is_valid(opponent_position) and self.is_valid(final_position):
            opponent_piece = self.checkers_board.get_piece(opponent_position)
            if self.is_opponent(piece, opponent_piece):
                if self.checkers_board.get_piece(final_position) == self.piece['empty']:
                    self.capture_neighbours.append(final_position)

    def is_opponent(self, piece, opponent_piece):
        return (piece in piece_set_one and opponent_piece in piece_set_two) or (piece in piece_set_two and opponent_piece in piece_set_one) 
