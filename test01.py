#!/usr/bin/env python
import subprocess 
import sys

f = open('test01.txt', 'w')

subprocess.Popen (["ls", "-l"], stdout=f)

f.close

