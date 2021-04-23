def readable_timedelta(days):
    # insert your docstring here
    """"
    coding a function for weeks days and its reminder


    """
    weeks = days // 7
    remainder = days % 7

    return "{} week(s) and {} day(s)".format(weeks, remainder)
day =readable_timedelta(30)
print(day)
