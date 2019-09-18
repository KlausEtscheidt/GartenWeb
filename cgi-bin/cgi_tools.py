#!/usr/bin/env python

#Sammlung von allgemeingueltigen Tools 
###########################################################
import socket,os,sys

#Wo sind wir ?
my_file= os.path.realpath(__file__)
my_dir=os.path.dirname(my_file)
sys.path.append( os.path.normpath("/home/pi/pylib"))

                 
server_address = ('192.168.1.44', 8889)
#server_address = ('localhost', 8889)

def print_header(title):
    print ("Content-type: text/html\n")
    print ("<!DOCTYPE html>")
    print ('<html lang=/"de-DE/">')
    print ('<head><meta charset=\"utf-8\">')
    print ('<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\"/>')
    print ("<title>{}</title>".format(title)) 
    print("<link rel=\"stylesheet\" href=\"../mystyle.css\" type=\"text/css\">")
    print ("</head>")

    print ("<body>")

def print_footer(link,caption):
     print('<footer>')
     print('<a href=\"'+link+'\">'+caption+'</a>')
     print('</footer>')

	
def print_headline(text):
     print('<header>')
     print('<h1>{}</h1>'.format(text)) 
     print('</header>')

def print_close():
    print ('</body>')
    print ('</html>')

def print_image_link(name):
    print('<img src=\"/img/'+name+'\" alt=\"Bild fehlt\">')

def socket_send(token):
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the port where the server is listening
    
    sock.connect(server_address)

    try:

        # Send data
        message = bytes("{}".format(token), 'ascii')
        sock.sendall(message)

        # Look for the response
        amount_received = 1

        heard=''
        while  amount_received > 0:
            data = sock.recv(8)
            amount_received = len(data)
            heard+=str(data,'ascii')
        return(heard)
        #print ('received "%s"' % heard)

    finally:
        sock.close()
