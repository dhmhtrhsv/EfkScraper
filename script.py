# -*- coding: utf-8 -*-
# Make a get request to get the latest position of the international space station from the opennotify api.
import requests
import time
import smtplib
from bs4 import BeautifulSoup

# Print the status code of the response.
#print(response.status_code)

#x = str(response.content.decode('utf-8'))
#print(x)
#if "Ανάρτηση ειδοποιητηρίων πληρωμής εισφορών" in x:
	#anartithikan = True
#print(anartithikan)

def notifications():
	anartithikan = False

	response = requests.get("https://www.efka.gov.gr/el/anakoinoseis")
	x = str(response.content.decode('utf-8'))
	soup = BeautifulSoup(x, 'html.parser')
	#print(soup.prettify())
	la = soup.find('article')
	if "Ανάρτηση ειδοποιητηρίων πληρωμής εισφορών" in la:
		anartithikan = True
		print("Anartithikan ta eidopoiitiria")
	print (anartithikan)

	if anartithikan == True:
		print("bika")
		s = smtplib.SMTP('smtp.gmail.com', 587)
		s.starttls()
		s.login("efka.notifications@gmail.com", "xdrgb12!@") 
		#message = "Τα ειδοποιητήρια του ΕΦΚΑ αναρτήθηκαν."
		sender = "efka.notifications@gmail.com"
		recipients = ["dhmhtrhsv@hotmail.com", "efka.notifications@gmail.com"]
		message = 'Subject: {}\n\n{}'.format("Ειδοποιητήρια ΕΦΚΑ", "Τα ειδοποιητήρια του ΕΦΚΑ αναρτήθηκαν")
		s.sendmail(sender, recipients, message.encode('utf-8'))
		s.quit()
		print("stalthike")
		time.sleep(15*24*60*60) # stamato na trexo gia 15 meres

	return None
	
while True:
	notifications()		
	time.sleep(5)
 






