  #date: run the job just once at a certain point of time.
  #interval: at fixed intervals of time.
  #cron: run the job periodically at certain time(s) of day


from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime

# Wrap your script in a function (I'll name this "timer")
def timer():
   #
   # Place script here
   #
sched = BlockingScheduler()

#DATE(This will run 04-1-2019 @ 08:23:30)
sched.add_job(timer, "date", run=datetime(2019, 04, 1, 8, 23, 30))

#CRON(This job will run sun, mon, and tue @ 07:05 and 14:05)
sched.add_job(timer, "cron", day_of_week="sun-tue", hour="7,14", minute=5)

#CRON(Schedules "timer" to be run on the third Friday of June, July, August, November and December at 00:00, 01:00, 02:00 and 03:00)
sched.add_job(timer,"cron", month="6-8,11-12", day="3rd fri", hour="0-3")

#INTERVAL(This will run every hour forever)
sched.add_job(timer, "interval", hours=1)

#INTERVAL(This will run every 2 hours from start_date to end_date)
sched.add_job(timer, "interval", hours=2, start_date="2016-10-10 09:30:00", end_date="2018-06-15 11:30:00")

sched.start()
