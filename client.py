from socket import *
from sys import argv

default_host = "localhost"
portnum = 5431


def talk():
    global portnum
    rhost = default_host
    if len(argv) > 1:
        rhost = argv[1]
    if len(argv) > 2:
        portnum = int(argv[2])
    print("Looking up address of " + rhost + "...", end="")
    try:
        dest = gethostbyname(rhost)
    except socket.gaierror as mesg:
        errno, errstr = mesg.args
        print("\n	", errstr)
        return
    print("got it: " + dest)
    addr = (dest, portnum)
    s = socket()
    res = s.connect_ex(addr)
    if res != 0:
        print("connect to port ", portnum, " failed")
        exit
    while True:
        try:
            buf = input("> ")
        except:
            break
        buf = buf + "\n"
        s.send(bytes(buf, "ascii"))

        data = s.recv(64)
        print("Message from Server: {}".format(data.decode('ascii')))


talk()
