#!/usr/bin/env python

####wird nicht mehr verwendet


import socket
import cgi_tools

import cgitb
cgitb.enable()

cgi_tools.print_header('Stop')
cgi_tools.print_headline('Stop')
print ("<main>")
cgi_tools.socket_send('stop')
#cgi_tools.print_image_link(img_name)
print ("</main>")
cgi_tools.print_footer('/index.html','Hauptseite')
cgi_tools.print_close()
