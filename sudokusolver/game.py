from sudokusolver.board import Board

class Game:
    def __init__(self, puzzle):
        self.puzzle = puzzle

    def solve(self):
        return self.solve_it(self.puzzle)

    def solve_it(self, matrix):
        for row in range(9):
            for col in range(9):
                if matrix[row][col] != 0:
                    continue
                for candidate in self.possible_values(matrix, row, col):
                    matrix[row][col] = candidate
                    if self.solve_it(matrix):
                        return matrix
                    matrix[row][col] = 0 # back to original value
                return   # nothing worked
        return matrix


    def possible_values(self, matrix, row, col):
        return Board(matrix).potential_values_for_position(row, col)