import os
import json
import urllib2

print('''

===================================================================
____   ________  _____________________    _____  _________ _____________________ 
\   \ /   /_   | \__    ___/\______   \  /  _  \ \_   ___ \\_   _____/\______   \
 \   Y   / |   |   |    |    |       _/ /  /_\  \/    \  \/ |    __)_  |       _/
  \     /  |   |   |    |    |    |   \/    |    \     \____|        \ |    |   \
   \___/   |___|   |____|    |____|_  /\____|__  /\______  /_______  / |____|_  /
                                    \/         \/        \/        \/         \/ \/
===================================================================

''')


while True:
    ip=raw_input("Enter the IP of the target: ")
    url = "http://ip-api.com/json/"
    response = urllib2.urlopen(url + ip)
    data = response.read()
    values = json.loads(data)
    
    n = values['lat'], values['lon']

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
