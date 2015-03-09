import time

#sync watches with teacher!!

#creating start and end times, this can be a good place to inject the teacher-created info
start = time.strptime("March 8, 2015 21:15:00", "%B %d, %Y %H:%M:%S")
end = time.strptime("March 8, 2015 21:16:00", "%B %d, %Y %H:%M:%S")
start = time.mktime(start)
end = time.mktime(end)

#config variables
PATH = '/home/pi/replay'

# SOD = time.mktime(time.striptime(""))
CLASS_SCHEDULE = {"First Period": (start,end)}
EOD = time.mktime(time.strptime("March 8, 2015 21:17:00", "%B %d, %Y %H:%M:%S"))