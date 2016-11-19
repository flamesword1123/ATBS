#! /usr/bin/env python3
# Password Locker - An insecure password locker program from ATBS Chapter 6

PASSWORDS = {"email" : "random@mail.something",
			 "blog": "sdfghjkasdjklkjhgfds",
			 "luggage": "12345765432"}


import sys
import pyperclip
if len(sys.argv) < 2:
	print("Usage: python passwordLocker.py [account] - copy account password")
	sys.exit()

account = sys.argv[1]	# first command line arg is the account name

if account in PASSWORDS:
	pyperclip.copy(PASSWORDS[account])
	print("Password for " + account + " copied to clipboard.")
else:
	print("There is no account named " + account)
