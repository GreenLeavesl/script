import os
from socket import gethostbyname, gethostname
host = gethostbyname(gethostname())
os.system('arp -a > temp.txt')
with open('temp.txt') as fp:
       for line in fp:
              line = line.split()[:2]
       if line and\
           line[0].startswith(host[:4]) and\
           (not line[0].endswith('255')):
              print(':'.join(line))