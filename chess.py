import string
class Game:
    white_player = ""
    black_player = ""
    is_black_player_turn = False
    is_white_player_turn = True
    movements = []

class Movements:
    player = ""
    movement_valid = False
    movement = ""

class Piece:
    color = ""
    alive = True
    canMove = True
    available_movements = []

class Pawn(Piece):
    piece_type = "pawn"
    
    def __init__(self, position, color):
        self.position = position
        self.color = color
        self.two_steps = True

    @staticmethod
    def initialise_pawn(board):
        for pos in range(0, len(board[1])):
            board[1][pos] = Pawn([pos, 1], "white")
        for pos in range(0, len(board[6])):
            board[6][pos] = Pawn([pos, 6], "black")
    
    def which_movement(self, next_pos):
        n_steps = 1
        if abs(self.position[1] - next_pos[1]) == 1:
            return n_steps, "lateral"
        if abs(self.position[1] - next_pos[1]) == 0 and abs(self.position[0] - next_pos[0]) in [1, 2]: 
            n_steps = self.position[0] - next_pos[0]
        return n_steps, "forward"
    
    def validate_move(self, next_pos):
        n_steps, movement = self.which_movement(next_pos)
        if movement == "lateral":
            if board[next_pos[0]][next_pos[1]]:
                board[next_pos[0]][next_pos[1]] = self
                return True, "killed!"
            if board[self.position[0] + 1][self.position[1]]:
                board[next_pos[0]][next_pos[1]] = self
                return True, "killed!"
            return False, "Invalid move! There is no piece to kill!"
        if movement == "forward":
            if board[next_pos[0]][next_pos[1]]:
                return False, "Invalid move! position is already blocked"
            if self.two_steps == False:
                return False, "Invalid move!"
            # if n_steps == 2:

            self.two_steps = False
            return True, "success"
        
def pos_converter(position):
    letters = list(string.ascii_lowercase)[:8]
    pos_map = {letters[i]:i for i in range(0, 8)}
    position = [pos_map[position[0]], position[1]]
    return position

def initialise_board():
    board = [[0 for j in range(0, 8)] for i in range(0, 8)]
    Pawn.initialise_pawn(board)


if __name__ == "__main__":
    initialise_board()
    
