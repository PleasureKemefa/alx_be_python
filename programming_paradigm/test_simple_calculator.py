# programming_paradigm/test_simple_calculator.py

import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_add(self):
        """Test the add method with various cases."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(-5, -10), -15)
        self.assertEqual(self.calc.add(1.5, 2.5), 4.0)

    def test_subtract(self):
        """Test the subtract method with various cases."""
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(0, 0), 0)
        self.assertEqual(self.calc.subtract(-5, -2), -3)
        self.assertEqual(self.calc.subtract(3, 5), -2)
        self.assertEqual(self.calc.subtract(2.5, 1.0), 1.5)

    def test_multiply(self):
        """Test the multiply method with various cases."""
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-1, 5), -5)
        self.assertEqual(self.calc.multiply(0, 10), 0)
        self.assertEqual(self.calc.multiply(-2, -4), 8)
        self.assertEqual(self.calc.multiply(2.5, 4), 10.0)

    def test_divide(self):
        """Test the divide method with various cases."""
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(3, 2), 1.5)
        self.assertEqual(self.calc.divide(-9, 3), -3)
        self.assertEqual(self.calc.divide(0, 5), 0)
        self.assertIsNone(self.calc.divide(10, 0))  # Division by zero
        self.assertEqual(self.calc.divide(5.0, 2.5), 2.0)

if __name__ == '__main__':
    unittest.main()