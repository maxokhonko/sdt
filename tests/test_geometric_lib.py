import math
import unittest

import circle
import rectangle
import square
import triangle


class CircleTestCase(unittest.TestCase):
    """Unit tests for circle.py."""

    def test_area_positive(self):
        self.assertAlmostEqual(circle.area(5), math.pi * 25)
        self.assertAlmostEqual(circle.area(1), math.pi)

    def test_area_zero(self):
        self.assertEqual(circle.area(0), 0)

    def test_area_float(self):
        self.assertAlmostEqual(circle.area(2.5), math.pi * 6.25)

    def test_perimeter_positive(self):
        self.assertAlmostEqual(circle.perimeter(5), 2 * math.pi * 5)

    def test_perimeter_zero(self):
        self.assertEqual(circle.perimeter(0), 0)

    def test_perimeter_float(self):
        self.assertAlmostEqual(circle.perimeter(2.5), 2 * math.pi * 2.5)


class RectangleTestCase(unittest.TestCase):
    """Unit tests for rectangle.py."""

    def test_area_zero(self):
        self.assertEqual(rectangle.area(10, 0), 0)
        self.assertEqual(rectangle.area(0, 10), 0)

    def test_area_square(self):
        self.assertEqual(rectangle.area(10, 10), 100)

    def test_area_normal(self):
        self.assertEqual(rectangle.area(4, 5), 20)

    def test_area_float(self):
        self.assertAlmostEqual(rectangle.area(2.5, 4.0), 10.0)

    def test_perimeter_zero(self):
        self.assertEqual(rectangle.perimeter(0, 0), 0)

    def test_perimeter_normal(self):
        self.assertEqual(rectangle.perimeter(4, 5), 18)

    def test_perimeter_square(self):
        self.assertEqual(rectangle.perimeter(10, 10), 40)

    def test_perimeter_float(self):
        self.assertAlmostEqual(rectangle.perimeter(2.5, 3.5), 12.0)


class SquareTestCase(unittest.TestCase):
    """Unit tests for square.py."""

    def test_area_zero(self):
        self.assertEqual(square.area(0), 0)

    def test_area_positive(self):
        self.assertEqual(square.area(6), 36)

    def test_area_float(self):
        self.assertAlmostEqual(square.area(2.5), 6.25)

    def test_perimeter_zero(self):
        self.assertEqual(square.perimeter(0), 0)

    def test_perimeter_positive(self):
        self.assertEqual(square.perimeter(6), 24)

    def test_perimeter_float(self):
        self.assertAlmostEqual(square.perimeter(2.5), 10.0)


class TriangleTestCase(unittest.TestCase):
    """Unit tests for triangle.py."""

    def test_area_zero(self):
        self.assertEqual(triangle.area(10, 0), 0)
        self.assertEqual(triangle.area(0, 5), 0)

    def test_area_positive(self):
        self.assertEqual(triangle.area(8, 5), 20.0)

    def test_area_float(self):
        self.assertAlmostEqual(triangle.area(3.5, 4.0), 7.0)

    def test_perimeter_zero(self):
        self.assertEqual(triangle.perimeter(0, 0, 0), 0)

    def test_perimeter_positive(self):
        self.assertEqual(triangle.perimeter(3, 4, 5), 12)

    def test_perimeter_float(self):
        self.assertAlmostEqual(triangle.perimeter(1.5, 2.5, 3.0), 7.0)


if __name__ == "__main__":
    unittest.main()