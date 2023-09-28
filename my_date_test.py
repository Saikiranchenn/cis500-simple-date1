import unittest
import my_date

class MyDateTest(unittest.TestCase):


  def test_is_leap_year_divisible_by_4(self):

    self.assertTrue(my_date.is_leap_year(2000))

    self.assertTrue(my_date.is_leap_year(2004))

    self.assertTrue(my_date.is_leap_year(2008))


  def test_is_leap_year_not_divisible_by_100(self):

    self.assertTrue(my_date.is_leap_year(2000))

    self.assertTrue(my_date.is_leap_year(2004))

    self.assertTrue(my_date.is_leap_year(2008))



  def test_is_leap_year_divisible_by_100_and_400(self):

    self.assertTrue(my_date.is_leap_year(1600))

    self.assertTrue(my_date.is_leap_year(2000))

    self.assertTrue(my_date.is_leap_year(2400))



  def test_is_leap_year_not_divisible_by_100_and_400(self):

    self.assertFalse(my_date.is_leap_year(1900))

    self.assertFalse(my_date.is_leap_year(2100))

    self.assertFalse(my_date.is_leap_year(2200))





    

if __name__ == '__main__':
    unittest.main()