from calculator import addition, subtraction, multiplication, division, power, \
                       cosine, square_root, mean, range_between_operands
import unittest
import math
import time
import sys
import datetime


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.startTime = time.time()
        self.st = datetime.datetime.fromtimestamp(self.startTime).strftime('%Y-%m-%d %H:%M:%S')

    def test_addition_integers(self):
        sum_ = addition(3, 4)
        self.assertEqual(sum_, 7)

    def test_addition_floats(self):
        sum_ = addition(10.5, 3.5)
        self.assertEqual(sum_, 14)

    def test_subtraction_integers(self):
        diff = subtraction(10, 5)
        self.assertEqual(diff, 5)

    def test_subtraction_floats(self):
        diff = subtraction(27.8, 3.8)
        self.assertEqual(diff, 24)

    def test_multiplication_integers(self):
        product = multiplication(3, 9)
        self.assertEqual(product, 27)

    def test_multiplication_floats(self):
        product = multiplication(32.9, 22.1)
        self.assertEqual(product, 727.09)

    def test_division_integers(self):
        quotient = division(10, 5)
        self.assertEqual(quotient, 2)

    def test_division_floats(self):
        quotient = division(389.23, 23.9)
        self.assertEqual(quotient, 16.285774058577406)

    def test_square_root_integers(self):
        sq = square_root(144)
        self.assertEqual(sq, 12)

    def test_square_root_integers(self):
        sq = square_root(2345.23)
        self.assertEqual(sq, 48.42757478957624)

    def test_mean_integers(self):
        avg = mean(50, 100)
        self.assertEqual(avg, 75)

    def test_mean_floats(self):
        avg = mean(345.234, 234.232)
        self.assertEqual(avg, 289.733)

    def test_power_integers(self):
        exp = power(2, 3)
        self.assertEqual(exp, 8)

    def test_power_floats(self):
        exp = power(2, 4.56)
        self.assertEqual(exp, 23.58830747665761)

    def test_cosine_pi(self):
        cos = cosine(math.pi)
        self.assertEqual(cos, -1.0)

    def test_cosine_2pi(self):
        cos = cosine(2*math.pi)
        self.assertEqual(cos, 1.0)

    def test_cosine_zero(self):
        cos = cosine(0)
        self.assertEqual(cos, 1.0)

    def test_range_between_operands(self):
        r = range_between_operands(1,10)
        self.assertEqual(r, [2,3,4,5,6,7,8,9])

    def tearDown(self):
        st = self.st
        print('time executed ==> ', st)

if __name__ == '__main__':
    import sys
    f = open("test_output", 'w')
    sys.stdout = f
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCalculator)
    unittest.TextTestRunner(f, verbosity=2).run(suite)
