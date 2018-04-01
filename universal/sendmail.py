#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header

from config import *

def sendMail(message, subject="News"):
	message = MIMEText(message,'plain','utf-8')
	message['From'] = Header("pi", 'utf-8')
	message['To'] = Header("Human", 'utf-8')

	message['Subject'] = Header(subject, 'utf-8')
	smtpObj = smtplib.SMTP_SSL(mail_host)
	#smtpObj.set_debuglevel(1)
	try:
		smtpObj.login(mail_user,mail_passwd)
		smtpObj.sendmail(sender, receivers, message.as_string())
		# log
		print("send success")
	except smtplib.SMTPException:
		# log
		print("send fail")
	finally:
		smtpObj.quit()

if __name__ == "__main__":
	sendMail('test from pi')
