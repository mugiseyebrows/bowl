import argparse
import random

def simulate(colors, take):
    bowl = []
    for i,c in enumerate(colors):
        for _ in range(c):
            bowl.append(i)
    res = [0 for i in range(len(colors)+1)]
    rounds = 1000000
    win = 1 / rounds
    for i in range(rounds):
        s = random.sample(bowl, take)
        res[len(set(s))] += win
    return res

parser = argparse.ArgumentParser()
parser.add_argument('-c','--colors', nargs='+')
parser.add_argument('-t','--take',type=int)

args = parser.parse_args()
#print(args); exit(0)

take = args.take
colors = [int(c) for c in args.colors]

res = simulate(colors, take)
for i,v in enumerate(res):
    if i == 0:
        continue
    print("p({}) = {:.3f}".format(i, v))