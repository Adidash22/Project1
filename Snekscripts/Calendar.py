"""
MVP Features:
- Build a calendar that would display the date, week and time   
- Build a capability to have tasks for a specified date
- Ability to edit tasks on the go
"""

 

"""
https://medium.com/@Suraj_Yadav/build-your-own-calendar-with-python-799caa57fffb reference code

Import the necessary modules
"""

import calendar
from datetime import datetime

now = datetime.now()
year = now.year
month = now.month

print(calendar.month_name[month] + " " +  str(year))
print("Mo Tu We Th Fr Sa Su")

num_days = calendar.monthrange(year, month)[1]
first_day = datetime(year, month, 1).weekday()

day = 1
for i in range(6):
    line = ""
    for j in range(7):
        if i == 0 and j < first_day:
            line += "  "
        elif day > num_days:
            break
        else:
            if day < 10:
                line += " "
            line += str(day) + " "
            day += 1
    print(line)
