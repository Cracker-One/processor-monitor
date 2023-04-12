import psutil
import time

import time
import sys
from colorama import Fore

print('PROCESSOR :')

def display_usage(cpu_usage):
    
    a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t = '  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  '
    if cpu_usage > 5 :
        a = '##'
    if cpu_usage > 10 :
        b = '##'
    if cpu_usage > 15 :
        c = '##'
    if cpu_usage > 20 :
        d = '##'
    if cpu_usage > 25 :
        e = '##'
    if cpu_usage > 30 :
        f = '##'
    if cpu_usage > 35 :
        g = '##'
    if cpu_usage > 40 :
        h = '##'
    if cpu_usage > 45 :
        i = '##'
    if cpu_usage > 50 :
        j = '##'
    if cpu_usage > 55 :
        k = '##'
    if cpu_usage > 60 :
        l = '##'
    if cpu_usage > 65 :
        m = '##'
    if cpu_usage > 70 :
        n = '##'
    if cpu_usage > 75 :
        o = '##'
    if cpu_usage > 80 :
        p = '##'
    if cpu_usage > 85 :
        q = '##'
    if cpu_usage > 90 :
        r = '##'
    if cpu_usage > 95 :
        s = '##'
    if cpu_usage > 98 :
        t = '##'
    
    print(f'\r['+a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+']',cpu_usage,end='\r')

while True:
    display_usage(psutil.cpu_percent())
    time.sleep(1.1)


