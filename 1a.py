import random
import matplotlib.pyplot as plt

#1a
def toss(p):
    return 'H' if random.random() < p else 'T'

N = 50
flips = [toss(0.7) for x in range(N)]
print(flips)
print(flips.count('H')/N)
longest_run=0
for i in range(N):
    count=0
    for j in range(i,N-1):
        if flips[j] == 'T':
            break
        if flips[i] == flips[j+1]:
            count = count+1
    if count>longest_run:
        longest_run = count+1
print(longest_run)