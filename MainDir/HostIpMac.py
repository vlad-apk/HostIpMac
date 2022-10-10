import re
import socket
import sys
import uuid
import datetime

a = input("Введите инвентарный номер: ")


def get_Host_name_IP():
    try:
        host_name = socket.gethostname()
        addrs = socket.getaddrinfo(socket.gethostname(), None)
        print("Hostname : ", host_name)
        for addr in addrs:
            print(addr[4][0])
        mac = (":".join(re.findall('..', '%012x' % uuid.getnode())))
        print("MAC: ", mac)
        print("Date: ", datetime.datetime.now())
    except:
        print("Unable to get Hostname and IP")


file_path = a + ".txt"
sys.stdout = open(file_path, "w")
print(get_Host_name_IP())

