import unittest
import numpy as np

from material import calculate_data_points

class TestCalculation(unittest.TestCase):
    def test_calculation_1(self):
        expected: np.ndarray = np.array([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
        self.assertEqual(expected.all(), calculate_data_points("x", 0, 1, 0.1).all())

    def test_calculation_2(self):
        expected: np.ndarray = np.array([8, 2, 0, 2, 8, 18, 32])
        self.assertEqual(expected.all(), calculate_data_points("2*x^2", -2, 4, 1).all())
