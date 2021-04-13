import math

def level(nodes):
    return math.ceil(math.log(nodes+1,2))

def leveltwo(nodes):
    if nodes > 0:
        return math.floor(math.log(nodes,2))+1
    return 0


for i in range(20):
    print(str(i)+" nodes, level: "+str(level(i))+"function 2 says its level: "+str(leveltwo(i)))