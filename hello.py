#!/usr/bin/env python

import os, sys
from pprint import pprint
import json
import urlparse


#params = urlparse.parse_qs(os.environ["QUERY_STRING"])
#print params
#usr_agent = os.environ["HTTP_USER_AGENT"]

#if "Firefox" in usr_agent:
#	print "Fire"
#elif "Chrome" in usr_agent:
#	print "Chrome"
#elif "curl" in usr_agent:
#	print "curl"
#else:
#	print "dunno" 
print "Content-Type: text/html"

username = "omar"
password = "omar"

content_length = os.environ["CONTENT_LENGTH"]
cookie = os.environ["HTTP_COOKIE"]
logged_in = False

if cookie == "logged_in=True":
	logged_in = True

elif content_length:
	bytes_to_read = int(content_length)
	
	content = sys.stdin.read(bytes_to_read)
	params = urlparse.parse_qs(content)
	
	if (params["username"][0] == username and params["password"][0] == password):

		print "Set-Cookie: logged_in = True"
		logged_in = True
	
print 

if not logged_in:
	print r"""
		<h1> Welcome! </h1>

		<form method="POST" action="hello.py">
		    <label> <span>Username:</span> <input autofocus type="text" name="username"></label> <br>
		    <label> <span>Password:</span> <input type="password" name="password"></label>

		    <button type="submit"> Login! </button>
		</form>
		"""
else:
	print "Found me!"
