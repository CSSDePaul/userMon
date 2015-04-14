import os
import threading

groups = ["Users",
          "Enterprise Admins",
          "Scheme Admins",
          "Domain Admins",
          "DHCP Admins",
          "WSS_Admin_WPG",
          "WSS_Restricted_WPG",
          "WSS_WPG",
          "Administrators"]

data = {}

def init():
    print "Monitoring Users . . . "
    for group in groups:
        result = os.popen('dsquery group -name "'+group+'" | dsget group -members -expand').read()
        data.update({group:result})

def check():
    global groups
    global data
    for group in groups:
        result = os.popen('dsquery group -name "'+group+'" | dsget group -members -expand').read()
        if result != data[group]:
            result = result.split("\n")
            temp = data[group].split("\n")
            for user in result:
                if user not in temp:
                    print "\nNew User:\n{} in {}\n".format(user,group)
            data[group]="\n".join(result)
    threading.Timer(5,check).start()

if __name__ == "__main__":
    init()
    check()
