import unittest

from services.Calculation import addition,multiplication,subtraction,divide

class CalculationTest(unittest.TestCase):
    def test_addition_with_positive_number(self):
        self.assertEqual(addition(4,6),10)
        self.assertEqual(addition(2.6,5.7),8.3)
        self.assertEqual(addition(2, 0), 2)

    def test_addition_with_negative_number(self):
        self.assertEqual(addition(-4, -6), -10)
        self.assertEqual(addition(-2.6, 5.7), 3.1)
        self.assertEqual(addition(2.6, -5.7), -3.1)
        self.assertEqual(addition(-2, -0), -2)

    def test_addition_with_non_numeric_number(self):
        with self.assertRaises(NameError):
            addition(a, b)

    def test_subtraction_with_positive_number(self):
        self.assertEqual(subtraction(4,6),-2)
        self.assertEqual(subtraction(2.6,5.7),-3.1)
        self.assertEqual(subtraction(2, 0), 2)

    def test_subtraction_with_negative_number(self):
        self.assertEqual(subtraction(-4, -6), 2)
        self.assertEqual(subtraction(-2.6, 5.7), -8.3)
        self.assertEqual(subtraction(2.6, -5.7), 8.3)
        self.assertEqual(subtraction(0, -2), 2)

    def test_subtraction_with_non_numeric_number(self):
        with self.assertRaises(NameError):
            subtraction(a, 1)

    def test_multiplication_with_positive_number(self):
        self.assertEqual(multiplication(4, 6), 24)
        self.assertEqual(multiplication(2.6,5.7), 14.82)
        self.assertEqual(multiplication(2, 0), 0)

    def test_multiplication_with_negative_number(self):
        self.assertEqual(multiplication(-4, -6), 24)
        self.assertEqual(multiplication(-2.6, 5.7), -14.82)
        self.assertEqual(multiplication(2.6, -5.7), -14.82)
        self.assertEqual(multiplication(0, -2), 0)

    def test_multiplication_with_non_numeric_number(self):
        with self.assertRaises(NameError):
            multiplication(a, 1)

    def test_divide_with_positive_number(self):
        self.assertEqual(divide(4, 6), 0.6666666666666666)
        self.assertEqual(divide(2.6,5.7), 0.45614035087719296)
        self.assertEqual(divide(81, 9), 9)
        self.assertEqual(divide(0, 9), 0)

    def test_divide_with_negative_number(self):
        self.assertEqual(divide(-4, -6), 0.6666666666666666)
        self.assertEqual(divide(-2.6, 5.7), -0.45614035087719296)
        self.assertEqual(divide(2.6, -5.7), -0.45614035087719296)
        self.assertEqual(divide(0, -2), 0)


    def test_divide_with_non_numeric_number(self):
        with self.assertRaises(NameError):
            divide(a, 1)

    def test_divide_with_zero_denominator_number(self):
        with self.assertRaises(ZeroDivisionError):
            divide(5,0)