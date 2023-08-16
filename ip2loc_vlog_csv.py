#!/usr/bin/env python3

'''
ip2loc_vlog_csv.py
By Michael Leidel (2023)
Outputs a csv file with columns of info on each unique IP
input file: vlog.txt
output file: user supplied
'''
import ipaddress
import sqlite3
import sys, os

def q(s):
  v = s.replace("'", "")
  return "'" + v + "'"

def proc_ip():
  ''' process this IP for location information '''
  print("               ", "\r", end="")
  print(ipv4, "\r", end="")
  # print("\r", end="")
  target = int(ipaddress.IPv4Address(ipv4))
  # print ("ip: {} => {}".format(ipv4, target), "")
  cursor = conn.execute("SELECT * FROM ip WHERE %s BETWEEN ip_from AND ip_to" % target)
  for row in cursor:
    oo.write(q(ipv4) + ",")
    oo.write(q(time) + ",")
    oo.write(row[2] + ",")
    oo.write(q(row[3]) + ",")
    oo.write(q(row[4]) + ",")
    oo.write(q(row[5]) + ",")
    oo.write(row[6] + ",")
    oo.write(row[7] + ",")
    oo.write(q(usrage) + "\n")


if not os.path.isfile("vlog.txt"):
  print("Missing Input vlog.txt file")
  sys.exit()

if len(sys.argv) < 2:
  print("Missing argument 1 output csv file name")
  sys.exit()

outfile = sys.argv[1]  # user must supply output file name

iplist = []

iplist = open("vlog.txt").read().splitlines()

iplist.sort()  # sort the IP address to bypass duplicates (below)

lastip = ""
count = 0
ipv4 = ""
conn = sqlite3.connect('ip2locationIPV4.db')
time = ""
usrage = ""

oo = open(outfile, "w")
oo.write("IP,DATE_TIME,CODE,NAME,REGION,CITY,LAT,LON,USER_AGENT\n")

for item in iplist:
  ipv4 = item.split(",")[0]
  time = item.split(",")[1]
  usrage = item.split(",")[2].strip()
  if ipv4 == lastip:
    continue
  lastip = ipv4  # skip repeat IP in sorted iplist
  proc_ip()
  count += 1

oo.close()
conn.close()
print("Finished: created ", outfile)
