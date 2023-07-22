import unittest

from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_create_rectangle_raises_no_exception(self):
        Rectangle(4, 5)

    def test_compute_area_with_positive_values_works_correctly(self):
        rect = Rectangle(4, 5)
        self.assertEqual(rect.compute_area(), 20)


if __name__ == "__main__":
    unittest.main()
