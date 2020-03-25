import unittest, os
from sudokusolver.board import Board


class TestBoard(unittest.TestCase):
    def setUp(self):
        self.matrix = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
                       [6, 0, 0, 1, 9, 5, 0, 0, 0],
                       [0, 9, 8, 0, 0, 0, 0, 6, 0],
                       [8, 0, 0, 0, 6, 0, 0, 0, 3],
                       [4, 0, 0, 8, 0, 3, 0, 0, 1],
                       [7, 0, 0, 0, 2, 0, 0, 0, 6],
                       [0, 6, 0, 0, 0, 0, 2, 8, 0],
                       [0, 0, 0, 4, 1, 9, 0, 0, 5],
                       [0, 0, 0, 0, 8, 0, 0, 7, 9]
                       ]
        self.board = Board(self.matrix)

    def test_is_valid(self):
        self.assertTrue(self.board.is_valid())

    def test_all_rows_valid(self):
        self.assertTrue(self.board.all_rows_valid())

    def test_invalid_all_rows_valid(self):
        self.matrix[0][-1] = 7
        self.assertFalse(Board(self.matrix).all_rows_valid())
        self.assertFalse(Board(self.matrix).is_valid())

    def test_all_columns_valid(self):
        self.assertTrue(self.board.all_columns_valid())

    def test_invalid_all_columns_valid(self):
        self.matrix[-1][0] = 5
        self.assertFalse(Board(self.matrix).all_columns_valid())
        self.assertFalse(Board(self.matrix).is_valid())

    def test_all_three_by_threes_valid(self):
        self.assertTrue(self.board.all_three_by_threes_valid())

    def test_invalid_all_three_by_threes_valid(self):
        self.matrix[1][1] = 3
        self.assertFalse(Board(self.matrix).all_three_by_threes_valid())
        self.assertFalse(Board(self.matrix).is_valid())

    def test_is_valid_three_by_three(self):
        valid_three_by_three = [[1, 0, 3], [4, 5, 0], [7, 8, 9]]
        self.assertTrue(self.board.is_valid_three_by_three(valid_three_by_three))

    def test_invalid_is_valid_three_by_three(self):
        invalid_three_by_three = [[1, 2, 3], [4, 0, 6], [0, 1, 9]]
        self.assertFalse(self.board.is_valid_three_by_three(invalid_three_by_three))

    def test_is_valid_row(self):
        valid_row = [0, 0, 1, 2, 3, 4, 5, 6, 7]
        self.assertTrue(self.board.is_valid_row(valid_row))

    def test_invalid_is_valid_row(self):
        valid_row = [0, 0, 1, 2, 3, 4, 5, 6, 1]
        self.assertFalse(self.board.is_valid_row(valid_row))

    def test_is_valid_column(self):
        valid_column = [0, 0, 1, 2, 3, 4, 5, 6, 7]
        self.assertTrue(self.board.is_valid_column(valid_column))

    def test_invalid_is_valid_row(self):
        invalid_column = [0, 0, 1, 2, 3, 4, 5, 6, 1]
        self.assertFalse(self.board.is_valid_column(invalid_column))
