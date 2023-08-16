#!/usr/bin/env python3

'''
ip2loc_vlog.py
By Michael Leidel (2023)
Outputs a report on showing info on each unique IP
Input: vlog.txt
Output: stdio

'''
import ipaddress
import sqlite3
import sys, os

def proc_ip():
  ''' process this IP for location information '''
  target = int(ipaddress.IPv4Address(ipv4))
  print("- - - - - - - - - - - - - - - - - - - - - - -")
  cursor = conn.execute("SELECT * FROM ip WHERE %s BETWEEN ip_from AND ip_to" % target)
  for row in cursor:
    print ("          IP: ", ipv4)
    print ("        Time: ", time)
    print ("country code: ", row[2])
    print ("country name: ", row[3])
    print (" region name: ", row[4])
    print ("   city name: ", row[5])
    print ("  User Agent: ", usrage)
    print ("https://maps.google.com/?q={},{}".format(row[6], row[7]))

if not os.path.isfile("vlog.txt"):
  print("Missing Input vlog.txt file")
  sys.exit()


iplist = []

iplist = open("vlog.txt").read().splitlines()

iplist.sort()  # sort the IP address to bypass duplicates (below)

lastip = ""
count = 0
conn = sqlite3.connect('ip2locationIPV4.db')
time = ""
usrage = ""

for item in iplist:
  ipv4 = item.split(",")[0]
  time = item.split(",")[1]
  usrage = item.split(",")[2].strip()

  if ipv4 == lastip:
    continue  # skip repeat IP in sorted iplist
  lastip = ipv4
  proc_ip()
  count += 1

conn.close()

print("\n\nFinished", str(count) + " unique IP addresses")
print("To check blacklist: python3 apivoid1.py xxx.xxx.xxx.xxx")
