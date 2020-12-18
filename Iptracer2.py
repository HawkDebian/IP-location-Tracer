import os
import json
import urllib.request as urllib2
import sys

sys.ps1 = '\033[01;32m '
print(sys.ps1)

os.system('cls || clear')

print('''

 ####### ######   #####   #####  
    #    #     # #     # #     # 
    #    #     #       #       # 
    #    ######   #####   #####  
    #    #   #         #       # 
    #    #    #  #     # #     # 
    #    #     #  #####   #####  
                                 

''')


while True:
    ip = input("Enter the IP of the target: ")
    url = f"https://api.ipdata.co/{ip}?api-key=160f9f7ed5a252a4c264df5c2326c893717ee7dbc26b776b38916ac6"
    os.system('cls || clear')
    response = urllib2.urlopen(url)
    data = response.read()
    values = json.loads(data)
    print(values)
    break
