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
