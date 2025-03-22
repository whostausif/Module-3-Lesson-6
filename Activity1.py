from datetime import date,time,datetime

today = date.today()
print("Today's date is: ",today)
now = datetime.now()
print("The current date and time is: ",now)
print("Date components: ",today.year,today.month,today.day)