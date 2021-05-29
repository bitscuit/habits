# visually show when each activity occurs in a day
# - parse csv into models
# - read daily activities
# - circular chart visually represents day
# - slice chart with activities

from model import Day, Activity
import toggl
import matplotlib.pyplot as plt
import numpy as np
import datetime

d = toggl.model_day('sample.csv')
durations = list()
labels = list()
for a in d.activities:
    # print(a.getName(), a.getStartTime(), a.getEndTime())
    delta = a.end_time - a.start_time
    # print(delta)
    durations.append(delta)
    labels.append(a.name)

print(durations)
# print(np.sum(durations))
normalized = [x / datetime.timedelta(hours=24) for x in durations]
print(normalized)
# print(np.sum(normalized))

# y = np.array([35, 25, 25, 10])
# labels = ["a", "b", "c", "d"]

y = normalized

colors = {
    'chores': 'green',
    'video': 'blue',
    'reading': 'red',
    'sleep': 'purple',
    'work': 'yellow',
    'food': 'orange',
    'news': 'pink',
    'games': 'gray',
    'exercise': 'black',
    'untracked': 'white'
}

plt.pie(y, labels = labels, colors=[colors[v] for v in labels], counterclock=False, startangle=90)
plt.show()
