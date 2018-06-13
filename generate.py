#!/usr/bin/python

# This little helper generates a list of invalid base64-encoded username:password sequences, followed by the correct one.
# The purpose is to speed up the process of creating a payload list useful for account-lockout in web applications whereas HTTP Auth Basic is in place.
# Invalid passwords are random strings.

from base64 import b64encode
import random
import string

username='user'
password='pass'
how_many=100

for i in range(0,how_many-1):
	credential=username+':'+''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6,10))
	print(b64encode(credential))

print b64encode(username+':'+password)
