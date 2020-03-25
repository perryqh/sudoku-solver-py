import unittest
from sudokusolver.game import Game


class TestGame(unittest.TestCase):
    def setUp(self):
        self.matrix = [[0, 0, 0, 1, 0, 0, 0, 5, 7],
                       [0, 1, 3, 0, 0, 0, 6, 0, 0],
                       [0, 0, 0, 6, 0, 5, 0, 8, 0],
                       [0, 5, 0, 0, 9, 0, 4, 2, 8],
                       [0, 0, 0, 7, 6, 4, 0, 0, 0],
                       [9, 3, 4, 0, 5, 0, 0, 6, 0],
                       [0, 6, 0, 9, 0, 2, 0, 0, 0],
                       [0, 0, 1, 0, 0, 0, 2, 7, 0],
                       [3, 2, 0, 0, 0, 7, 0, 0, 0]
                       ]
        self.solved_matrix = [[6, 4, 8, 1, 2, 3, 9, 5, 7],
                              [5, 1, 3, 8, 7, 9, 6, 4, 2],
                              [2, 7, 9, 6, 4, 5, 1, 8, 3],
                              [7, 5, 6, 3, 9, 1, 4, 2, 8],
                              [1, 8, 2, 7, 6, 4, 5, 3, 9],
                              [9, 3, 4, 2, 5, 8, 7, 6, 1],
                              [4, 6, 7, 9, 8, 2, 3, 1, 5],
                              [8, 9, 1, 5, 3, 6, 2, 7, 4],
                              [3, 2, 5, 4, 1, 7, 8, 9, 6]
                              ]
        self.game = Game(self.matrix)

    def test_solve(self):
        self.assertEqual(self.game.solve(), self.solved_matrix)