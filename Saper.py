import random

row =  3 # wymiay
column =  3 # wymiary

class Board:
    def __init__(self, row: int, column: int):
        self.row = row
        self.column = column
        
    def board_repr(self) -> list:
        board_size = [0] * self.row*self.column
        return board_size
    
    def init_bombs(self, bombs_num):
        coords = [random.sample(range(0, (self.row*self.column)-1), bombs_num)]
        print(coords)
        sorted_coords = sorted(coords)
        board = self.board()
        for ele in sorted_coords:
            board[ele] = 1
        
        return board
    
    
    def print_board(self, bomb_board):
        i = 1
        while i <= self.row*self.column:
            print(bomb_board[i-1], end=' ')
            if i % self.row == 0:
                print("")
            i += 1
                        
        
    
    
board = Board(6,3)

# print("TYP", type(board.board_repr()))
bomb_board = board.init_bombs(7)
print("bomby", bomb_board)
print(board.print_board(bomb_board))


# coord = [0,0,1,2,4,6]
# print(sorted(coord))