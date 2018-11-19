# -*- coding: utf-8 -*-
import requests
import time
import smtplib
from bs4 import BeautifulSoup

def notifications():
	anartithikan = False
	response = requests.get("https://www.efka.gov.gr/el/anakoinoseis")
	x = str(response.content.decode('utf-8'))
	soup = BeautifulSoup(x, 'html.parser')
	la = soup.find('article')
	if "Ανάρτηση ειδοποιητηρίων πληρωμής εισφορών" in la:
		anartithikan = True
		print("Anartithikan ta eidopoiitiria")
	print (anartithikan)
	notifications_posted = []
	if anartithikan == True:
		s = smtplib.SMTP('smtp.gmail.com', 587)
		s.starttls()
		s.login("efka.notifications@gmail.com", "dcrget12!@")  # Here you write your gmail account and password
		sender = "efka.notifications@gmail.com"
		recipients = ["dhmhtrhsv@hotmail.com", "efka.notifications@gmail.com","gtsapelas@epu.ntua.gr"]
		message = 'Subject: {}\n\n{}'.format("Ειδοποιητήρια ΕΦΚΑ", "Τα ειδοποιητήρια του ΕΦΚΑ αναρτήθηκαν")
		s.sendmail(sender, recipients, message.encode('utf-8'))
		s.quit()
		print("Mail sent")
		time.sleep(15*24*60*60)
	return None
	
while True:
	notifications()		
	time.sleep(5)
 






