import random
from itertools import groupby
from operator import itemgetter
import matplotlib.pyplot as plt

#1c
def toss(p):
    return 'H' if random.random() < p else 'T'

N = 500
flips = [toss(0.7) for x in range(N)]
print(flips)
print(flips.count('H')/N)
flps=[]
for i in range(N):
    if(flips[i]=='T'):
        flps.append(0)
    else:
        flps.append(1)

run_lengths=[]
for k,v in groupby(enumerate(flps),key=itemgetter(1)):
    if k:
        v = list(v)
        run_length = v[-1][0]-v[0][0]+1
        run_lengths.append(run_length)
print(run_lengths)
plt.hist(run_lengths, width=0.3, color='blue')
plt.xlabel('Run Length of Heads',fontsize=12)
plt.show()