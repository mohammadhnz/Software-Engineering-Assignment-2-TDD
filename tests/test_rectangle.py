import unittest

from models.rectangle import Rectangle
from models.square import Square


class TestRectangle(unittest.TestCase):
    def test_create_rectangle_raises_no_exception(self):
        Rectangle(4, 5)

    def test_compute_area_with_positive_values_works_correctly(self):
        rect = Rectangle(4, 5)
        self.assertEqual(rect.compute_area(), 20)

    def test_compute_area_zero_values_returns_zero(self):
        rect = Rectangle(0, 10)
        self.assertEqual(rect.compute_area(), 0)

    def test_compute_area_decimal_values_works_correctly(self):
        rect = Rectangle(8.5, 6.3)
        self.assertAlmostEqual(rect.compute_area(), 53.55, delta=0.01)

    def test_rectangle_initialization_with_negative_width(self):
        with self.assertRaises(ValueError):
            Rectangle(-2, 7)

    def test_rectangle_initialization_with_negative_height(self):
        with self.assertRaises(ValueError):
            Rectangle(3, -9)

    def test_rectangle_initialization_with_non_numeric_width(self):
        with self.assertRaises(TypeError):
            Rectangle("3", 5)

    def test_rectangle_initialization_with_non_numeric_height(self):
        with self.assertRaises(TypeError):
            Rectangle(6, [4])

    def test_change_rectangle_height_works_correctly(self):
        rect = Rectangle(3, 5)
        rect.set_height(10)
        self.assertEqual(rect.compute_area(), 50)

    def test_change_rectangle_width_works_correctly(self):
        rect = Rectangle(3, 5)
        rect.set_width(10)
        self.assertEqual(rect.compute_area(), 30)

    def test_create_square_raises_no_exception(self):
        square = Square(10)

    def test_compute_area_of_square(self):
        square = Square(10)
        self.assertEqual(square.compute_area(), 100)


if __name__ == "__main__":
    unittest.main()
