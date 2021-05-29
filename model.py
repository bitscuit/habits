import datetime

# day has activities

# activity has name, start time, end time

class Day(object):
    activities = list()

class Activity(object):
    name = str()
    start_time = datetime.time()
    end_time = datetime.time()
    # startDate = datetime.date()
    # endDate = datetime.date()
