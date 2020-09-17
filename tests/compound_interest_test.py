import unittest

from src.compound_interest import CompoundInterest

class CompoundInterestTest(unittest.TestCase):

    # The program should ask for the starting amount, 
    # the number of years to invest and the interest rate. 
    #Formula     
    # A = P(1 + r/n)nt

    # P is the principal amount
    # r is the annual rate of interest
    # t is the number of years the amount is invested
    # n is the number of times the interest is compounded per year
    # A is the amount at the end of the investment

    def test_can_find_principle(self):
        compound_interest = CompoundInterest(100, 20, 10)
        self.assertEqual(100, compound_interest.principle)

    def test_can_find_years(self):
        compound_interest = CompoundInterest(100, 20, 10)
        self.assertEqual(20, compound_interest.years)

    def test_can_find_interest(self):
        compound_interest = CompoundInterest(100, 20, 10)
        self.assertEqual(10, compound_interest.interest)
        
    def test_output_of_one_plus_rate_over_times_compounded(self):
        compound_interest = CompoundInterest(100, 20, 10)
        self.assertEqual(round(1.83, 2), round((1 + compound_interest.interest / 12), 2))    
    # Should return 732.81 given 100 principal, 10 percent, 20 years
    # def test_returns_732_point81_given_100(self):
    #     compound_interest = CompoundInterest(100, 20, 10)
    #     self.assertEqual(732.81, compound_interest.amount_returned())


    # Should return 181.94 given 100 principal, 6 percent, 10 years

    # Should return 149,058.55 given 100000 principal, 5 percent, 8 years

    # Should return 0.00 given 0 principal, 10 percent, 1 year

    # Should return 100.00 given 100 principal, 0 percent, 10 years


    # Extention tests

    # Should return 118,380.16 given 100 principal, 5 percent, 8 years, 1000 per month

    # Should return 156,093.99 given 100 principal, 5 percent, 10 years, 1000 per month

    # Should return 475,442.59 given 116028.86, 7.5 percent, 8 years, 2006 per month

    # Should return 718,335.96 given 116028.86 principal, 9 percent, 12 years, 1456 per month

