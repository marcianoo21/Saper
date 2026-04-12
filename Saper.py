import random
from enum import Enum

class Position(Enum): # liczba sąsiadujących pól w zależności od położenia pola
    CORNER = 3
    EDGE = 5
    MIDDLE = 8 


class Board:
    def __init__(self, row: int, column: int):
        self.row = row
        self.column = column
        # Inicjalizacja tablicy 2D (lista list)
        self.grid = [[None for _ in range(self.column)] for _ in range(self.row)]
        self.isLost = False
    
    def init_bombs(self, bombs_num):
        # Generujemy wszystkie możliwe pary (wiersz, kolumna) i losujemy z nich pozycje bomb
        all_coords = [(r, c) for r in range(self.row) for c in range(self.column)]
        coords = random.sample(all_coords, bombs_num)
        print("Wylosowane współrzędne bomb:", coords)
        
        for r, c in coords:
            self.grid[r][c] = "BOOM"
    
    
    def print_board(self):
        for r in range(self.row):
            for c in range(self.column):
                print(self.grid[r][c], end='\t') # \t ładnie formatuje odstępy
            print("")
        print("\n")
                   
                   
    def isBomb(self, guess: tuple): # załóżmy że guess to dwie opisujące współrzędne pola na planszy w zakresie od (1, 1) do (self.row, self.column) - indeksujemy od 1 dla prostoty dla gracza
        x, y = guess
        if x > self.row or x < 1 or y > self.column or y < 1:
            raise ValueError(f"Współrzędne ({x}, {y}) wykraczają poza rozmiar planszy!")    
        print("GUESS", self.grid[x-1][y-1])
        # ...
    
    
    def field_reveal(self, coords: tuple):
        x, y = coords
        # counter = 0
        # if (x == 1 or x == self.row) and (y == 1 or y == self.column):
            
        #     print(Position.CORNER)
        # elif (x == 1 or x == self.row) or (y == 1 or y == self.column):
        #     print(Position.EDGE)
        # else:
        #     print(Position.MIDDLE)
        
        
        if self.grid[x-1][y-1] == "BOOM":
            print("You lost;(")
            self.isLost = True
            return self.isLost
            
    def neighbor_numbers(self):
        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            ( 0, -1),          ( 0, 1),
            ( 1, -1), ( 1, 0), ( 1, 1)
        ]
        
        for x in range(self.row):
            for y in range(self.column):
                if self.grid[x][y] == "BOOM":
                    for dx, dy in directions:
                        nx, ny = dx + x, dy + y
                        if 0 <= nx < self.row and 0 <= ny < self.column:
                            if self.grid[nx][ny] != "BOOM":
                                if type(self.grid[nx][ny]) is not int:
                                    self.grid[nx][ny] = 1
                                else:
                                    self.grid[nx][ny] += 1
        
                   
                        
row =  6 # wymiar horyzontalny
column =  8 # wymiar wertykalny
   
board = Board(row, column)

user_guess = (1,2) # pierwszy rząd, druga kolumna

board.init_bombs(7)
# print("bomby", board.grid)

# board.isBomb(user_guess)
for i in range(3):
    board = Board(i+3,i+4)
    board.init_bombs(i+3)
    board.print_board()

    # board.field_reveal((1,2))
    # board.field_reveal((1,1))
    # board.field_reveal((4,3))
    # board.field_reveal((row, column))

    board.neighbor_numbers()
    board.print_board()
# while not board.isLost:
#     board.print_board()
#     try:
#         user_guess = tuple(map(int, input("Put coordinates to reveal the field (eg. 1 2): ").split()))
#         x, y = user_guess
#         print("user guess", user_guess, "is", board.grid[x-1][y-1])
#         board.field_reveal(user_guess)
#     except IndexError as e:
#         print(f"Error: {e}")
#     except ValueError as e:
#         print(f"Error: {e}")