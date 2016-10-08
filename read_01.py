#!/usr/bin/env python
myfile = open("atop.log", "rU")
file = open('/home/german/Dropbox/IT/Python/read_02.txt', 'w')
for line in myfile.xreadlines():
    PID = line [4:5]
    if PID.isdigit():
        CPU = int(line [60:62])
        if CPU > 0:
            print line
            file = open('/home/german/Dropbox/IT/Python/read_02.txt', 'a')
            file.write(line + '\n')

