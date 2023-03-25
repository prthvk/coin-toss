import random
import matplotlib.pyplot as plt
    
#1b

def toss(p):
    return 'H' if random.random() < p else 'T'

trials = [20,100,200,1000]
for t in trials:
    no_heads = []
    trial = list(range(1, t+1))
    print(trial)
    for y in range(t):
        N = 50
        flips = [toss(0.7) for i in range(N)]
        no_heads.append(flips.count('H'))
    print(no_heads)
    plt.hist(no_heads, width = 0.5, color='blue')
    plt.xlabel('Number of Heads',fontsize=12)
    plt.show()
