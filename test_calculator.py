# GitHub Link: https://github.com/Revengestyle6/lab10-LP-RH.git
# Partner 1: Lawrence P.
# Partner 2: Ritesh H.
import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(3, 5), 8)
        self.assertEqual(add(4, 8), 12)
        self.assertEqual(add(9, 7), 16)


    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(8, 6), 2)
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(9, 7), 2)


    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertAlmostEqual(mul(2,3),6)
        self.assertAlmostEqual(mul(42, 7), 294)
        self.assertAlmostEqual(mul(10, 12), 120)
    #     fill in code

    def test_divide(self): # 3 assertions
        self.assertAlmostEqual(div(3,6),2)
        self.assertAlmostEqual(div(50, 150), 3)
        self.assertAlmostEqual(div(1000, 6000), 6)
    #     fill in code
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)


    #     fill in code

    def test_logarithm(self): # 3 assertions
        self.assertEqual(logarithm(10, 10), 1)
        self.assertEqual(logarithm(2, 8), 3)
        self.assertEqual(logarithm(10, 100), 2)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(5, 0)
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
        with self.assertRaises(ValueError):
            logarithm(0, 5)
    #     fill in code

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(3,4),5)
        self.assertEqual(hypotenuse(12, 16), 20)
        self.assertEqual(hypotenuse(5,12),13)
    #     fill in code

    def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError):
            square_root(-1)
        with self.assertRaises(ValueError):
            square_root(-32)
        with self.assertRaises(ValueError):
            square_root(-5003)
    #     # Test basic function
    #     fill in code
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()