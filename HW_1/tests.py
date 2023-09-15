import unittest
from calculator import calculate_discount


class TestCalculator(unittest.TestCase):
    def test_result(self):
        self.assertEqual(80.0, calculate_discount(purchase_amount=100, discount_amount=20))

    def test_zero_result(self):
        self.assertEqual(0, calculate_discount(purchase_amount=0, discount_amount=10))

    def test_zero_discount(self):
        self.assertEqual(100, calculate_discount(purchase_amount=100, discount_amount=0))

    def test_discount_less_0(self):
        self.assertRaisesRegex(ArithmeticError, "Процент не может быть меньше 0!",
                               calculate_discount, purchase_amount=100, discount_amount=-20)

    def test_discount_more_100(self):
        self.assertRaisesRegex(ArithmeticError, "Процент не может быть больше 100!",
                               calculate_discount, purchase_amount=100, discount_amount=120)


if __name__ == '__main__':
    unittest.main(verbosity=2)
