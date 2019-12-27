import sys
import numpy as np
import requests
import time

def getValues(mean, sd, lam, i):
    mean = float(mean)
    sd = float(sd)
    lam = float(lam)
    i = int(i)
    
    for x in range (i):
        if mean ==0:
            callURL()
            waitTime = np.random.poisson(lam,1)
            print(waitTime)
            time.sleep(abs(waitTime))
        elif lam == 0:
            callURL()
            waitTime = np.random.normal(mean,sd,1)
            print(waitTime)
            time.sleep(abs(waitTime))

def callURL():
    r = requests.get("http://localhost:80/primecheck")


getValues(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])