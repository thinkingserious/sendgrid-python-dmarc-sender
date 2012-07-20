#!/usr/bin/python

"""
Copyright (c) 2012 SendGrid

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
documentation files (the "Software"), to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of
the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO
THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF
CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""

import requests
from configobj import ConfigObj

""" DMARC Test Sender using SendGrid.com

We setup 4 SendGrid sub-accounts that account for these scenarious:
	SPF = fail, DKIM = fail
	SPF = fail, DKIM = pass
	SPF = pass, DKIM = fail
	SPF = pass, DKIM = pass

DKIM failure is provoked by either:
	1. Adding random characters to the public key in DNS
	2. Setting the d=domain to be a domain that will never match the from a address

SPF failure is provoked by:
	1a. Make sure the IP published in the SPF record does not match the sending IP
	1b. Remove the CNAME for the SendGrid white labeled domain
	1c. Add a SPF record for email.[yourdomain].com, this SPF record is the same from step 1a

"""

"""Grab our SendGrid.com credentials and the DMARC test emails"""
config = ConfigObj('./config.ini')

def send(email):
	subject = "Email sent to: " + email
	
	"""SPF = fail, DKIM = fail"""
	payload = {'to': email, 'from': config['from_email'], 'subject': subject, 'text': config['msg_s0d0'], 'html': config['msg_s0d0'], 'api_user': config['api_user_s0d0'], 'api_key': config['api_key_s0d0']}
	r = requests.get("http://sendgrid.com/api/mail.send.json", params=payload)
	
	"""SPF = fail, DKIM = pass"""
	payload = {'to': email, 'from': config['from_email'], 'subject': subject, 'text': config['msg_s1d0'], 'html': config['msg_s1d0'], 'api_user': config['api_user_s1d0'], 'api_key': config['api_key_s1d0']}
	r = requests.get("http://sendgrid.com/api/mail.send.json", params=payload)
	
	"""SPF = pass, DKIM = fail"""
	payload = {'to': email, 'from': config['from_email'], 'subject': subject, 'text': config['msg_s0d1'], 'html': config['msg_s0d1'], 'api_user': config['api_user_s0d1'], 'api_key': config['api_key_s0d1']}
	r = requests.get("http://sendgrid.com/api/mail.send.json", params=payload)

	"""SPF = pass, DKIM = pass"""
	payload = {'to': email, 'from': config['from_email'], 'subject': subject, 'text': config['msg_s1d1'], 'html': config['msg_s1d1'], 'api_user': config['api_user_s1d1'], 'api_key': config['api_key_s1d1']}
	r = requests.get("http://sendgrid.com/api/mail.send.json", params=payload)

if __name__ == "__main__":
	emails = config['emails']
	"""Send out the test emails"""
	for email in emails:
		send(email)