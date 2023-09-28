import unittest
import my_date

class MyDateTest(unittest.TestCase):
    def test_is_leap_year(self):
        test_cases = [
            (2000, True),
            (2004, True),
            (2100, False),
            (2023, False),
            (1600, True),
            (1900, False),
            (2008, True),
            (2400, True),
            (2800, True),
            (4000, True),
        ]

        for year, expected_output in test_cases:
            actual_output = is_leap_year(year)
            self.assertEqual(expected_output, actual_output)


if __name__ == '__main__':
    unittest.main()

# Test cases for the general_date() function

# Valid dates
general_date(2023, 1, 1) == 1
general_date(2023, 3, 8) == 67
general_date(2023, 12, 31) == 365

# Leap year
general_date(2024, 2, 29) == 60

# Edge cases
general_date(2023, 0, 1) == 1
general_date(2023, 13, 1) == 365

# Invalid dates
general_date(2023, -1, 1) == -1
general_date(2023, 14, 1) == -1
general_date(2023, 1, 32) == -1

# Non-integer inputs
general_date(2.5, 1, 1) == -1
general_date(1, 2.5, 1) == -1
general_date(1, 1, 3.5) == -1
You can use these test cases to verify that the general_date() function is working correctly for all possible inputs.

year1 = 2022
month1 = 12
day1 = 31
year2 = 2023
month2 = 1
day2 = 1

day_of_week(2023, 9, 27) == "Wednesday"
day_of_week(2024, 2, 29) == "Friday"
day_of_week(1900, 1, 1) == "Monday"
day_of_week(2000, 12, 31) == "Saturday"

day_of_week(2023, 0, 1) == "Invalid date" 
day_of_week(2023, 13, 1) == "Invalid date" 
day_of_week(2023, 9, 0) == "Invalid date" 
day_of_week(2023, 9, 32) == "Invalid date" 

import unittest

from to_str import to_str


class TestToStr(unittest.TestCase):

    def test_valid_dates(self):
        general.commonOne(to_str(2023, 9, 27), "Wednesday, 27 September 2023")
        general.commonOne(to_str(1833, 3, 7), "Wednesday, 07 March 1833")
        general.commonOne(to_str(1000, 1, 1), "Saturday, 01 January 1000")

    def test_invalid_dates(self):
        with general.commonRaises(ValueError):
            to_str(-1, 9, 27)

        with general.commonRaises(ValueError):
            to_str(2023, 13, 27)

        with general.commonRaises(ValueError):
            to_str(2023, 9, 32)


if __name__ == '__main__':
    unittest.main()

