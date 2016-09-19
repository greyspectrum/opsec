#!/usr/bin/env python

from bs4 import BeautifulSoup, NavigableString
from urllib2 import urlopen
import time
import subprocess

print "OPSEC: AUTONOMOUS OPERATIONAL SECURITY ANALYTIC ENGINE"
subprocess.Popen(["espeak", "Loading OPSEC"])
time.sleep(2)
subprocess.Popen(["espeak", "autonomous operational security analytic engine"])
time.sleep(4)
print "Collecting analytics..."
subprocess.Popen(["espeak", "Collecting analytics..."])
time.sleep(3)
print "Performing cryptanalysis..."
subprocess.Popen(["espeak", "Performing cryptanalysis..."])
time.sleep(3)
print "Executing state..."
subprocess.Popen(["espeak", "Executing state.."])
time.sleep(3)
print "Fetching EFF Scorecard..."
subprocess.Popen(["espeak", "Fetching EFF Scorecard..."])
time.sleep(3.25)
print "Assembling Customized Threat Model..."
subprocess.Popen(["espeak", "Assembling Customized Threat Model..."])
time.sleep(4)
print "Loading Operational Oracle..."
subprocess.Popen(["espeak", "Loading Operational Oracle..."])
time.sleep(3)
print "Asking Snowden..."
subprocess.Popen(["espeak", "Asking Snowden..."])
time.sleep(3)
print "\n-----SYSTEM READY-----"
subprocess.Popen(["espeak", "system ready"])
time.sleep(2)
print "\nAs your attorney, I advise:\n"
subprocess.Popen(["espeak", "As your attorney, I advise"])
time.sleep(3)

user = "thegrugq_ebooks" 

endpoint = "https://twitter.com/%s"

f = urlopen(endpoint % user)
html =  f.read()
f.close()

soup =  BeautifulSoup(html, 'html.parser') 

tweets =  soup.find_all('strong', {'class': 'fullname js-action-profile-name show-popup-with-id'})

for i in range(0,len(tweets)):
	user = tweets[i].contents[0]

	action_tag = soup('span', {'class': 'username js-action-profile-name'})
	show_name = action_tag[i].contents[1].contents[0]

	twit_text = soup('p', {'class': 'js-tweet-text'})

	message = ""
	for nib in twit_text[i]:
		if isinstance(nib, NavigableString):
			message += nib
		else:
			message += nib.text

	print message
	subprocess.Popen(["espeak", message])
	time.sleep(7)

time.sleep(1)
print "Use Signal. Use Tor."
subprocess.Popen(["espeak", "Use Signal. Use Tor."])
time.sleep(4)
print "OPERATIONAL ANALYSIS COMPLETE"
subprocess.Popen(["espeak", "operational analysis complete"])
time.sleep(4)
