import numpy as np

class Board:
    def __init__(self, matrix):
        self.matrix = np.array(matrix)

    def is_valid(self):
        return self.all_rows_valid() and self.all_columns_valid() and self.all_three_by_threes_valid()

    def all_rows_valid(self):
        rows_valid = [self.is_valid_row(row) for row in self.matrix]
        return all(rows_valid)

    def all_columns_valid(self):
        columns_valid = [self.is_valid_column(column) for column in self.matrix.T]
        return all(columns_valid)

    def all_three_by_threes_valid(self):
        return True;

    def potential_values_for_position(self, row, column):
        return []

    def is_valid_three_by_three(self, three_by_three):
        return self.is_unique_set(three_by_three);

    def is_valid_row(self, row):
        return self.is_unique_set(row)

    def is_valid_column(self, column):
        return self.is_unique_set(column)

    def is_unique_set(self, numbers):
        without_zeros = [number for number in np.array(numbers).flatten() if number > 0]
        return len(without_zeros) == len(set(without_zeros))
