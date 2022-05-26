import nmap
import re
import ipaddress





portRange = re.compile("([0-9]+)-([0-9]+)")
minPort = 0
maxPort = 65535


print('''


        SAMARTH SONI 
        PORT SCANNER

''')

openPorts = []

while True:
    enterIP = input("Enter ip address to scan: ")

    try:
        ipObj = ipaddress.ip_address(enterIP)
        break
        
    except:
        print("Invalid IP address")


while True:
   
    print("Please enter the range of ports you want to scan in format: <int>-<int> (ex would be 60-120)")
    port_range = input("Enter port range: ")
    
    port_range_valid = portRange.search(port_range.replace(" ",""))
    if port_range_valid:
        
        minPort = int(port_range_valid.group(1))
       
        maxPort = int(port_range_valid.group(2))
        break



nm = nmap.PortScanner()


for i in range(minPort,maxPort+1):
    try:
        result = nm.scan(enterIP, str(i))
        port_status = (result['scan'][enterIP]['tcp'][i]['state'])
        print(f"Port {i} is {port_status}")
    except:
          print(f"Cannot scan port {i}.")
        

