import unittest
from calculator import calculate

class TestCalculate(unittest.TestCase):
    def test_addition(self):
        result = calculate(2, 2, "+")
        self.assertEqual(result, 4)
    def test_subtraction(self):
        result = calculate(8, 2, "-")
        self.assertEqual(result, 6)
    def test_division(self):
        result = calculate(10, 2, "/")
        self.assertEqual(result, 5)
    def test_invalid_action(self):
        with self.assertRaises(ValueError):
            calculate(2, 2, "#")
    def test_invalid_division(self):
        with self.assertRaises(ZeroDivisionError):
            calculate(2, 0, "/")

if __name__ == "__main__":
    unittest.main()
