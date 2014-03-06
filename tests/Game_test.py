from Bowling.Game import Game
import unittest

class TestGame(unittest.TestCase):

    def setUp(self):
        self.game = Game()

    def test_rolling_gutter_game(self):
        self.roll_balls(20, 0)
        self.assertEqual(self.game.score(), 0)

    def test_rolling_all_ones(self):
        self.roll_balls(20, 1)
        self.assertEqual(self.game.score(), 20)

    def test_rolling_one_spare(self):
        self.roll_spare()
        self.game.roll(3)
        self.roll_balls(17, 0)
        self.assertEqual(self.game.score(), 16)

    def test_one_string(self):
        self.roll_strike()
        self.game.roll(3)
        self.game.roll(4)
        self.roll_balls(16, 0)
        self.assertEqual(self.game.score(), 24)

    def test_perfect_game(self):
        self.roll_balls(12, 10)
        self.assertEqual(self.game.score(), 300)

    def roll_balls(self, times, pins):
        for frame in range(times):
            self.game.roll(pins)

    def roll_spare(self):
        self.game.roll(5)
        self.game.roll(5)

    def roll_strike(self):
        self.game.roll(10)
