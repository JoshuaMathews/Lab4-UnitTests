import unittest 
from unittest import TestCase
from price_discount import discount  

class TestDiscount(TestCase):

    def test_list_of_three_prices(self):
        prices = [10, 4, 20]
        expected_discount = 4
        self.assertEqual(expected_discount, discount(prices))

    def test_list_of_two_prices(self):
        prices = [10, 20]
        expected_discount = 0
        self.assertEqual(expected_discount, discount(prices))

    def test_list_of_zero_prices(self):
        prices = []
        expected_discount = 0
        self.assertEqual(expected_discount, discount(prices))

    def test_list_of_ten_prices(self):
        prices = [10, 201, 4, 100, 44444, 23423, 54546, 333, 243, 234234]
        expected_discount = 4
        self.assertEqual(expected_discount, discount(prices))


if __name__ == '__main__':
    unittest.main()