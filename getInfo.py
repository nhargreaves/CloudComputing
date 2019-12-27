import sys
import requests
from datetime import datetime
import dateutil.parser as dp
from pymongo import MongoClient
import json
from pprint import pprint
#import urllib.parse


client = MongoClient('localhost',27017, username='root',password='example')


db = client.cpuData
collection = db.cpuCollection
print(client.list_database_names())
r = requests.get("http://localhost:8080/api/v1.3/subcontainers/docker/32aab2f6215c132c33ad1e78e9bed7a1604706dcb6a2a0a5f838fbb446258e63").json()

cpuArray = [0] * 60
memoryArray = [0] * 60
ioArray = [0] * 60
timeStamps = [0] * 60
timeStampsExtra = [0] * 60
cpuUsage = [0] * 60

for x in range (60):
    cpuArray[x] = r[0]['stats'][x]['cpu']['usage']['total']
    cpuArray[x] = float(cpuArray[x])
    memUsage = r[0]['stats'][x]['memory']['usage']
    memTotal = r[0]['stats'][x]['memory']['max_usage']

    timeStamps[x] = r[0]['stats'][x]['timestamp']
    parsed_date = dp.parse(timeStamps[x])
    timeStampsExtra[x] = parsed_date.strftime('%s')
    timeStampsExtra[x] = float(timeStampsExtra[x])*1e9

    if(x > 0):
        cpuCalc = cpuArray[x] - cpuArray[x-1]
        timeCalc = timeStampsExtra[x] - timeStampsExtra[x-1]
        totalCalc = (cpuCalc/timeCalc) * 100
        cpuUsage[x] = round(totalCalc,2)
      
        
    memoryArray[x] = round(1.0 * memUsage/memTotal,3)


    ioArray[x] = r[0]['stats'][x]['diskio']['io_service_bytes'][0]['stats']['Total']

    print(cpuUsage[x], ": cpu")
    print(memoryArray[x], ': mem')
    print(ioArray[x], ': io')

    post = {"Cpu": cpuUsage[x-1],"Memory": memoryArray[x], "Time": timeStamps[x]}


    post_id = collection.insert_one(post)