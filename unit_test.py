import unittest
import math
from unit_test import (
    rectangle_area, rectangle_perimeter,
    circle_area, circle_perimeter,
    square_area, square_perimeter,
    triangle_area, triangle_perimeter,
    parallelogram_area, parallelogram_perimeter
)

class TestGeometryFunctions(unittest.TestCase):

    # --- Rectangle ---
    def test_rectangle_area(self):
        self.assertEqual(rectangle_area(5, 10), 50)

    def test_rectangle_perimeter(self):
        self.assertEqual(rectangle_perimeter(5, 10), 30)

    # --- Circle ---
    def test_circle_area(self):
        self.assertAlmostEqual(circle_area(3), math.pi * 9, places=5)

    def test_circle_perimeter(self):
        self.assertAlmostEqual(circle_perimeter(3), 2 * math.pi * 3, places=5)

    # --- Square ---
    def test_square_area(self):
        self.assertEqual(square_area(4), 16)

    def test_square_perimeter(self):
        self.assertEqual(square_perimeter(4), 16)

    # --- Triangle ---
    def test_triangle_area(self):
        self.assertEqual(triangle_area(6, 4), 12)

    def test_triangle_perimeter(self):
        self.assertEqual(triangle_perimeter(3, 4, 5), 12)

    # --- Parallelogram ---
    def test_parallelogram_area(self):
        self.assertEqual(parallelogram_area(6, 3), 18)

    def test_parallelogram_perimeter(self):
        self.assertEqual(parallelogram_perimeter(5, 7), 24)


if __name__ == "__main__":
    unittest.main()
