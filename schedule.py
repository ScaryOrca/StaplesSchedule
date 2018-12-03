#!/usr/bin/env python

# Title: Aisle 7
# Author: Matthew Warner
# Description: Print schedule for current day

from bs4 import BeautifulSoup
from datetime import datetime
import mechanize
import requests
import ssl
import sys, getopt

loginURL = "https://associateconnection.staples.com/psp/psext/?cmd=login"
calURL = "https://associateconnection.staples.com/psc/psext/EMPLOYEE/HRMS/c/ROLE_EMPLOYEE.SCH_EE_SCHEDULE.GBL"
user = ""
password = ""
opts, args = getopt.getopt(sys.argv[1:],"u:p:")

# needed to prevent SSL related errors
ssl._create_default_https_context = ssl._create_unverified_context
br = mechanize.Browser()

# first day of month, needed to calculate offset
calOffset = datetime.today().replace(day=1).isoweekday()

# today
calDay = int(datetime.today().strftime("%d"))

# fix offsets
# Python's datetime has Monday = 1, Sunday = 7
if calOffset is 7:
    calOffset = 0
else:
    calDay += calOffset

# check correct parameters are passed
for o, a in opts:
    if o == "-u":
        user = a
    elif o == "-p":
        password = a
    else:
        print "Error fetching schedule, exiting."

try:
    br.set_handle_robots(False)
    loginPage = br.open(loginURL, timeout=10.0)

    br.select_form(nr=0)
    br["userid"] = user
    br["pwd"] = password
    br.submit()

    r = br.open(calURL, timeout=10.0)
    s = BeautifulSoup(r.read(), "html.parser")

    # actual time scheduled for day, with fixed spacing
    t = s.find("span", attrs={"id": "DERIVED_SCH_CAL_SCH_TEXT2_" + str(calDay)}).text.replace("-", " -")

    if ":" not in t:
        print "Off"

    else:
        print t

except Exception:
    print "Error fetching schedule, exiting."
