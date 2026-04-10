import random
from enum import Enum

class Position(Enum):
    CORNER = 3
    EDGE = 5
    MIDDLE = 8 


class Board:
    def __init__(self, row: int, column: int):
        self.row = row
        self.column = column
        self.grid = [None] * (self.row * self.column) # stan planszy, zawsze updatowany dla tego samego obiektu
    
    def init_bombs(self, bombs_num):
        coords = random.sample(range(0, (self.row*self.column)-1), bombs_num)
        print("Posortowane indeksy bomb", coords)
        sorted_coords = sorted(coords)
        
        for ele in sorted_coords:
            self.grid[ele] = "BOOM"
    
    
    def print_board(self):
        i = 1
        while i <= self.row*self.column:
            print(self.grid[i-1], end=' ')
            if i % self.row == 0:
                print("")
            i += 1
        print("\n")
                   
                   
    def isBomb(self, guess: tuple): # załóżmy że guess to dwie opisujące współrzędne pola na planszy w zakresie od (1, 1) do (self.row, self.column) - indeksujemy od 1 dla prostoty dla gracza
        x, y = guess
        if x > self.row or x < 1 or y > self.column or y < 1:
            raise ValueError(f"Współrzędne ({x}, {y}) wykraczają poza rozmiar planszy!")    
        print("index", (x-1)*self.row + (y-1))
        print("GUESS", self.grid[(x-1)*self.row + (y-1)]) # mapowanie dwóch wymiarów na jeden odpowiadający tablicy 1D
        # ...
    
    
    def field_reveal(self, coords: tuple):
        x, y = coords
        if (x == 1 or x == self.row) and (y == 1 or y == self.column):
            print(Position.CORNER)
        elif (x == 1 or x == self.row) or (y == 1 or y == self.column):
            print(Position.EDGE)
        else:
            print(Position.MIDDLE)
        # ...
                   
                        
row =  6 # wymiar horyzontalny
column =  6 # wymiar wertykalny
   
board = Board(row, column)

user_guess = (1,2) # pierwszy rząd, druga kolumna

board.init_bombs(7)
print("bomby", board.grid)

board.isBomb(user_guess)

board.print_board()

board.field_reveal((1,2))
board.field_reveal((1,1))
board.field_reveal((4,3))
board.field_reveal((row, column))