from __future__ import print_function
import json
import urllib2 
import os
import sys

key = sys.argv[1]   # key = '056a5fec-16fc-4372-82a6-358369262821'
busline = sys.argv[2]   # busline = 'B52'
url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?\
key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s"%(key,busline)
response = urllib2.urlopen(url)
data = response.read().decode("utf-8")
jsondata = json.loads(data)

busdata = jsondata['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
print('Bus Line: ', busline) 
print('Number of Active Buses: ', len(busdata))
for i in range(0,len(busdata)):
    buslocation = jsondata['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']\
              [i]['MonitoredVehicleJourney']['VehicleLocation']
    lat = buslocation.get('Latitude', 'Not Found') 
    lon = buslocation.get('Longitude', 'Not Found')
    print('Bus %s is at latitude %s and longitude %s'%(i, lat, lon))
