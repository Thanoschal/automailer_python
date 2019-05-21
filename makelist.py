#!/usr/bin/env python

from os import listdir
from os.path import isfile, join
import sys
import re

if len(sys.argv) < 2:
    print "Usage: ./makelist.py <path of assignments directory>"
    sys.exit()

mypath = sys.argv[1]

f = open("mailinglist","w+")

onlyfiles = [fi for fi in listdir(mypath) if isfile(join(mypath, fi))]

mail_domain = "@di.uoa.gr"
mail_prefix = "sdi"

for x in onlyfiles:

    am = re.findall('\d+',x)[0]
    mail_am = am.replace('111520', '')
    final_mail = mail_prefix + mail_am + mail_domain
    f.write(str(final_mail) + "\n")  

#end_for

print "Successfuly created mailing list!!!"

f.close()

