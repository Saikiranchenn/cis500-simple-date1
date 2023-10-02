#######################################################
# my_dates
#
# Name: Sai Kiran
# Section: 03
#
# Fall 2023
#########################################################


def is_leap_year(year: int) -> bool:
    """if year is a leap year then it will return as True or else it will return as false"""
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False


def ordinal_date(year: int, month: int, day: int) -> int:
    """Return the number of days that have passed since the start of the year, including any partial days.."""
    # Number of days in each month (non-leap year)
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Update February if it's a leap year
    if is_leap_year(year):
        days_in_month[2] = 29

    # Calculate the ordinal date
    ordinal_date = day
    for i in range(1, month):
        ordinal_date += days_in_month[i]

    return ordinal_date

    

def days_elapsed(year1: int, month1: int, day1: int, year2: int, month2: int, day2:int ) -> int:
    import datetime
    d1 = datetime.date(year1, month1, day1)
    d2 = datetime.date(year2, month2, day2)
    d_diff = d2 - d1
    return d_diff.days


def day_of_week(year: int, month: int, day: int) -> str:
    import datetime
    date_dt = datetime.date(year, month, day)
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    day_dy = date_dt.weekday()
    return days_of_week[day_dy]


def to_str(year: int, month: int, day: int) -> str:
    """Return the date as a string with the format "Wednesday, 07 March 1833"."""
    # Days of the week
    DAYS_OF_WEEK = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    # Months of the year
    MONTHS = [
        'January', 'February', 'March', 'April', 'May', 'June',
        'July', 'August', 'September', 'October', 'November', 'December'
    ]

    # Calculate the day of the week
    from datetime import datetime
    date_obj = datetime(year, month, day)
    day_name = DAYS_OF_WEEK[date_obj.weekday()]
    month_name = MONTHS[month - 1]

    return f"{day_name}, {day:02d} {month_name} {year}"

