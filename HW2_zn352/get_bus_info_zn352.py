from __future__ import print_function
import json
import urllib2 
import os
import sys

key = sys.argv[1]
# key = '056a5fec-16fc-4372-82a6-358369262821'
busline = sys.argv[2]
# busline = B52
url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s"%(key,busline)
response = urllib2.urlopen(url)
data = response.read().decode("utf-8")
jsondata = json.loads(data)
busdata = jsondata['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']

# Author: federica bianco, NYU, September 2016
##############################
from __future__ import print_function
import sys

filename = sys.argv[3]
if not len(sys.argv) == 3:
    print("Invalid number of arguments.")
    sys.exit()

fout = open(sys.argv[3], "wb")
##############################

#write in csv file
fout.writerow("Latitude,Longitude,Stop Name,Stop Status")
for i in range(0,len(busdata)):
    for j in range(0,len(busdata[i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'])):  #problem
        buslocation = jsondata['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]\
        ['MonitoredVehicleJourney']['VehicleLocation']
        stoplocation = jsondata['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]\
        ['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][j]
        busdistance = jsondata['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]\
        ['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][j]['Extensions']['Distances']
        lat = buslocation.get('Latitude', 'Not Found')
        lon = buslocation.get('Longitude', 'Not Found')
        stoplc = stoplocation.get('StopPointName', 'N/A')
        distance = busdistance.get('PresentableDistance','N/A')
        fout.writerow('%s,%s,%s,%s'%(lat,lon,stoplc,distance))
        
        
