import argparse
from itertools import product

def minus_one(colors, i):
    return [c if i!=j else max(0,c-1) for j,c in enumerate(colors)]

class Item:
    def __init__(self, p, colors):
        self.p = p
        self.children = []
        self.colors = colors

    def evaluate(self):
        colors = self.colors
        tot = sum(colors)
        self.children = [Item(c / tot, minus_one(colors, i)) for i,c in enumerate(colors)]

    def probability(self, m):
        if len(self.children) == 0:
            return self.p
        return self.p * self.children[m[0]].probability(m[1:])

def leaf_nodes(tree):
    if len(tree.children) == 0:
        yield tree
        return
    for child in tree.children:
        for item in leaf_nodes(child):
            yield item
    
def evaluate(colors, take):
    tree = Item(1, colors)
    for _ in range(take):
        for item in leaf_nodes(tree):
            item.evaluate()

    res = [0 for _ in range(len(colors)+1)]
    for item in product(range(len(colors)), repeat=take):
        res[len(set(item))] += tree.probability(item)
    return res

parser = argparse.ArgumentParser()
parser.add_argument('-c','--colors', nargs='+', type=int)
parser.add_argument('-t','--take', type=int)

args = parser.parse_args()

res = evaluate(args.colors, args.take)
for i,v in enumerate(res):
    if i == 0:
        continue
    print("p({}) = {:.6f}  {:4.1f}%".format(i, v, v * 100))