import psutil
import time

current = []
print "Current Users:"
for user in psutil.users():
    current.append(user.name)
    print "\t"+user.name

print "\nNow Monitoring. . ."
while True:
    time.sleep(5)
    for user in psutil.users():
        if user.name not in current:
            print "New User '{}' Detected".format(user.name)
