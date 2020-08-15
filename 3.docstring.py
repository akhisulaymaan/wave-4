def readable_timedelta(days):
    # insert your docstring here
    ''' to print the number of weeks and days in the argument, days
    # to get the number of days in a week, we divide the number of days by 7
    weeks = days // 7
    # to the number of days that remain, for days that are more than 7 days, we use modulus operator
    remainder = days % 7 '''
    return "{} week(s) and {} day(s)".format(weeks, remainder)