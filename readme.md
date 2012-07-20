This program allows you to send test emails which create the following scenarios useful for testing DMARC aggregate reports:
* The SPF & DKIM should fail
* The SPF should fail & DKIM should pass
* The SPF should pass & DKIM should fail
* The SPF & DKIM should pass

Python library dependencies: requests, configobj

You will need to create a configuration file in the same directory as the dmarc_sender.py file. For the following sample configuration file, please note the following definitions.

**emails:**
A list of emails to send test emails to. Currently, the code requires at least 2 emails.

**from_email:**
The email you want to appear in the from feild

**sX_dX:**
s = SPF, d = DKIM  
if X = 0, fail  
if X = 1, pass  

**msg_sX_dX:**
The message to include in the body of the email.  

**api_user_sX_dX:**
Your SendGrid API username.  

**api_key_sX_dX:**
Your SendGrid API key.  

=== config.ini ===

emails = 'test1@example.com', 'test2@example.com'

from_email = you@yourdomain.com

msg_s0d0 = "This is a test email from SendGrid.com's DMARC tester. The SPF & DKIM should fail."  
api_user_s0d0 = user  
api_key_s0d0 = pass  

msg_s0d1 = "This is a test email from SendGrid.com's DMARC tester. The SPF should fail & DKIM should pass."  
api_user_s0d1 = user  
api_key_s0d1 = pass  

msg_s1d0 = "This is a test email from SendGrid.com's DMARC tester. The SPF should pass & DKIM should fail."  
api_user_s1d0 = user  
api_key_s1d0 = pass  

msg_s1d1 = "This is a test email from SendGrid.com's DMARC tester. The SPF & DKIM should pass."  
api_user_s1d1 = user  
api_key_s1d1 = pass  

=== end ===