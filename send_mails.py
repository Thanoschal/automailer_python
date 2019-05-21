#!/usr/bin/env python

# -*- coding: utf-8 -*-
import smtplib, ssl
import getpass
import configfile as cfg
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time

#create receiver list from the text
emails = []

try:  
    fp = open('mailinglist', 'r')
    line = fp.readline()
    emails.append(line.rstrip())
    mailcount = 1
    while line:
        line = fp.readline()
        
        if line == '':
            continue
        else:
            emails.append(line.rstrip())
            mailcount += 1
        #end_if
    #end_while
    
finally:  
    fp.close()

#print emails
#print mailcount


#read the email from the text

text = ""
subject = ""

try:  
    fp = open('mailtosend', 'r')
    line = fp.readline()
    subject = line.rstrip()
    while line:
        line = fp.readline()
        
        if line == '':
            continue
        else:
            text = text + line            
        #end_if
    #end_while
    
finally:  
    fp.close()

msg = MIMEMultipart("alternative")
msg["Subject"] = unicode(subject, 'utf-8')
part1 = MIMEText(text, "plain", "utf-8")
msg.attach(part1)

final_mail = msg.as_string()

#login to email service
password = getpass.getpass(prompt='Password: ', stream=None)
server = smtplib.SMTP_SSL(cfg.mailer["smtp_server"], cfg.mailer["tlsport"])
server.login(cfg.mailer["sender_login"], password)


print "\nNumber of recipients: " + str(mailcount)

#send the text to the emails specified in mailinglist
server.sendmail(cfg.mailer["sender_email"], emails, final_mail)
print "\nMails successfuly sent!!!"


#end_for



