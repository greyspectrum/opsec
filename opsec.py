from bs4 import BeautifulSoup, NavigableString
from urllib2 import urlopen

import time

print "Collecting analytics..."
time.sleep(1)
print "Performing cryptanalysis..."
time.sleep(1)
print "Executing state..."
time.sleep(1)
print "Fetching EFF Scorecard..."
time.sleep(1.25)
print "Assembling Customized Threat Model..."
time.sleep(1)
print "Loading Operational Oracle..."
time.sleep(2)
print "Asking Snowden..."
time.sleep(2)
print "\n-----SYSTEM READY-----"
time.sleep(2)
print "\nAs your attorney, I advise:\n"
time.sleep(1.5)

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
	time.sleep(1)

time.sleep(1)
print "\n Use Signal. Use Tor."
