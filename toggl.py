import csv
from model import Day, Activity
import datetime

def model_day(filename):
    activities = list()
    with open(filename) as file:
        csv_reader = csv.DictReader(file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                # print(f'Column names are {", ".join(row)}')
                line_count += 1
            # print(row)
            # print(datetime.datetime.strptime(row["Start time"], '%H:%M:%S').time())
            line_count += 1
            
            a = model_activity(row)
            activities.append(a)
    d = Day()
    d.activities = activities
    calc_untracked(activities)
    return d

def model_activity(activity_fields):
    a = Activity()
    a.name = (activity_fields["Description"])
    a.start_time = (datetime.datetime.strptime(activity_fields["Start time"], '%H:%M:%S'))
    a.end_time = (datetime.datetime.strptime(activity_fields["End time"], '%H:%M:%S'))
    return a

def calc_untracked(activities):
    for i in range(1, len(activities)):
        # print(i)
        delta = activities[i].start_time - activities[i-1].end_time
        print(activities[i].name, delta)