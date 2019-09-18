#!/usr/bin/env python
import socket
import cgi_tools
import datetime

def get_data():
    print('<table id=\"sensordaten\">')
    zeit=datetime.datetime.now().strftime("%d.%m.%Y %H:%M")
    #print('<tr><td>Zeit: </td><td> {:s} </td></tr>'.format(zeit))
    temp_zaun=float(cgi_tools.socket_send('Sensoren;lesen;T_Lu_St'))
    print('<tr><td>Temperatur Zaun: </td><td> {:2.1f} &deg;C</td></tr>'.format(temp_zaun))
    wi_staerke=float(cgi_tools.socket_send('Sensoren;lesen;Wi_Stae_St'))
    print('<tr><td>Windst&auml;rke:  </td><td> {:2.1f} km/h</td></tr>'.format(wi_staerke))
    wi_boe=float(cgi_tools.socket_send('Sensoren;lesen;Wi_Boe_St'))
    print('<tr><td>Windboen:  </td><td> {:2.1f} km/h</td></tr>'.format(wi_boe))
    regen=float(cgi_tools.socket_send('Sensoren;lesen;Reg_St'))
    print('<tr><td>Regen:  </td><td> {:2.2f} mm/min</td></tr>'.format(regen))
    bar=float(cgi_tools.socket_send('Sensoren;lesen;Bar_GH_aus_Druck'))
    print('<tr><td>Luftdruck:         </td><td> {:4.0f} hPa</td></tr>'.format(bar))
    lum=float(cgi_tools.socket_send('Sensoren;lesen;Lum_GH_Lum'))
    print('<tr><td>Helligkeit:  </td><td> {:2.0f} </td></tr>'.format(lum))
    hyg=float(cgi_tools.socket_send('Sensoren;lesen;Bar_GH_aus_Hyg'))
    print('<tr><td>rel. Luftfeuchte:  </td><td> {:2.0f} % </td></tr>'.format(hyg))
    hygbod=float(cgi_tools.socket_send('Sensoren;lesen;HygBod'))
    print('<tr><td>Bodenfeuchte:  </td><td> {:02.3f} V </td></tr>'.format(hygbod))
    print("</table>")
    print('Stand: {:s} <p>'.format(zeit))


cgi_tools.print_header('aktuelle Wetterdaten')
cgi_tools.print_headline('aktuelle Wetterdaten')
print ("<main>")
get_data()
print ("</main>")
cgi_tools.print_footer('/index.html','Hauptseite')
cgi_tools.print_close()
