import unittest
from kirsten_medlin import *


class MyTestCase(unittest.TestCase):
    def test_square(self):
        self.assertEqual(square(10), 100)
        self.assertAlmostEqual(square(0.1), 0.01, delta=0.001)

        with self.assertRaises(TypeError):
            square('0')

        with self.assertRaises(ValueError):
            square(0)
            square(-4)

    def test_circle(self):
        self.assertEqual(circle(10), 314.1592653589793)
        self.assertAlmostEqual(circle(0.1), 0.031, delta=0.001)

        with self.assertRaises(TypeError):
            circle('0')

        with self.assertRaises(ValueError):
            circle(0)
            circle(-4)

    def test_rectangle(self):
        self.assertEqual(rectangle(2, 1), 2)
        self.assertAlmostEqual(rectangle(1.5, 1), 1.5, delta=0.001)
        self.assertAlmostEqual(rectangle(1, 1.6), 1.6, delta=0.001)
        self.assertAlmostEqual(rectangle(1.5, 2.1), 3.15, delta=0.001)

        with self.assertRaises(TypeError):
            rectangle(1, '1.5')
            rectangle('0', 1.5)
            rectangle('0', '1.5')

        with self.assertRaises(ValueError):
            rectangle(-1, 1.5)
            rectangle(1, -1.5)
            rectangle(-1, -1.5)
            rectangle(0, 1.5)
            rectangle(2, 0)
            rectangle(0, 0)

    def test_triangle(self):
        self.assertEqual(triangle(2, 1), 1)
        self.assertAlmostEqual(triangle(1.5, 1), 0.75, delta=0.001)
        self.assertAlmostEqual(triangle(1, 1.6), 0.8, delta=0.001)
        self.assertAlmostEqual(triangle(1.5, 2.1), 1.575, delta=0.001)

        with self.assertRaises(TypeError):
            triangle(1, '1.5')
            triangle('0', 1.5)
            triangle('0', '1.5')

        with self.assertRaises(ValueError):
            triangle(-1, 1.5)
            triangle(1, -1.5)
            triangle(-1, -1.5)
            triangle(0, 1.5)
            triangle(2, 0)
            triangle(0, 0)


if __name__ == '__main__':
    unittest.main()
