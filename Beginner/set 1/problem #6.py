import calendar
try:
    year = int(input())
    if calendar.isleap(year):
        print("yes")
    else:
        print("no")
except:
    print("invalid")
