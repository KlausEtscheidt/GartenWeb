#!/usr/bin/env python
import socket
import cgi_tools
import cgitb
cgitb.enable()

logpath="/home/pi/usb/Garten/log/"


def get_data():
    with open(logpath+"my_err.log", "r", encoding='utf8') as fobj:
    #with open("x:\Garten/gh_data/my.log", "r", encoding='utf8') as fobj:
       lines=fobj.readlines()
       maxline=len(lines)
       for i in range(1,maxline+1):
           line=lines[maxline-i]
           #Sonderzeichen html-konform wandeln
           line=line.encode('ascii', 'xmlcharrefreplace')
           #bytes in string wandeln
           line=line.decode('ascii')
           print('<p class="log">',line.rstrip(),'</p>')



cgi_tools.print_header('ErrLogfile')
cgi_tools.print_headline('ErrLogfile')
print ("<main><errlogging>")
get_data()
print ("</errlogging></main>")
cgi_tools.print_footer('/index.html','Hauptseite')
cgi_tools.print_close()
