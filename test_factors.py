import unittest
from my_server import trial_division

class TestTrialDivision(unittest.TestCase):
    def test_factors_of_12(self):
        self.assertEqual(trial_division(12), [2, 2, 3])

    def test_factors_of_13(self):
        self.assertEqual(trial_division(13), [13])

    def test_factors_of_360(self):
        self.assertEqual(trial_division(360), [2, 2, 2, 3, 3, 5])

    def test_factors_of_1(self):
        self.assertEqual(trial_division(1), [1])

if __name__ == "__main__":
    unittest.main()
