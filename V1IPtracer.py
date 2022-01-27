import os
import json
import urllib.request as urllib2
import sys

sys.ps1 = '\033[01;32m '
print(sys.ps1)


print('''

████████╗██╗  ██╗███████╗██████╗ ███████╗██████╗ ██╗ █████╗ ███╗   ██╗
╚══██╔══╝██║  ██║██╔════╝██╔══██╗██╔════╝██╔══██╗██║██╔══██╗████╗  ██║
   ██║   ███████║█████╗  ██║  ██║█████╗  ██████╔╝██║███████║██╔██╗ ██║
   ██║   ██╔══██║██╔══╝  ██║  ██║██╔══╝  ██╔══██╗██║██╔══██║██║╚██╗██║
   ██║   ██║  ██║███████╗██████╔╝███████╗██████╔╝██║██║  ██║██║ ╚████║
   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═════╝ ╚══════╝╚═════╝ ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝
                                                                      

                                  
                                                                        
''')


while True:
    ip = input("Enter the IP of the target: ")
    url = "http://ip-api.com/json/"
    response = urllib2.urlopen(url + ip)
    data = response.read()
    values = json.loads(data)
    
    

    print(" IP: " + values['query'])
    print(" City: " + values['city'])
    print(" Region: " + values['regionName'])
    print(" Country: " + values['country'])
    print(" CountrtCode: " + values['countryCode'])
    print(" ZIP code: " + values['zip'])
    print(" latitude: ")
    print(values['lat'])
    print(" longitude: ")
    print(values['lon'])
    print(" TimeZone: " + values['timezone'])
    print(" ISP: " + values['isp'])
    print(" org: " + values['org'])
    print(" as: " + values['as'])
    break
