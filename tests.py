import unittest
from format_price import format_price


class TestPriceConvert(unittest.TestCase):

    def test_int(self):
        formated_price = format_price(3213.00)
        self.assertEqual(formated_price, '3 213')

    def test_float(self):
        formated_price = format_price(3213.54)
        self.assertEqual(formated_price, '3 213,54')

    def test_str(self):
        formated_price = format_price('3213.54')
        self.assertEqual(formated_price, '3 213,54')

    def test_comma_separated_str(self):
        formated_price = format_price('3213,54')
        self.assertEqual(formated_price, '3 213,54')

    def test_words_in_str(self):
        formated_price = format_price('321fd3,54')
        self.assertEqual(formated_price, None)

    def test_big_number(self):
        formated_price=format_price('3213.98344324')
        self.assertEqual(formated_price,'3 213,98')

if __name__ == '__main__':
    unittest.main()
