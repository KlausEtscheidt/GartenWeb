#!/usr/bin/env python

####wird nicht mehr verwendet

import socket
import cgi_tools

import cgitb
cgitb.enable()

cgi_tools.print_header('Start')
cgi_tools.print_headline('Start')
print ("<main>")
print ("<p>fehlt noch</p>")
command = "/usr/bin/sudo /sbin/shutdown -r now"
import subprocess
process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
output = process.communicate()[0]
print ("<p>"+str(output)+"</p>")
 
#cgi_tools.print_image_link(img_name)
print ("</main>")
cgi_tools.print_footer('/index.html','Hauptseite')
cgi_tools.print_close()
