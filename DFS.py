def calcpathcost(path):
  pathcost=0
  for i in range (1,len(path)):
    edge=path[i-1]+path[i]
    stepcost=cost[edge]
    pathcost=pathcost+stepcost
  return pathcost

def DFS():
    while fringe:
        node = fringe.pop(0)
        path = pathq.pop(0)

        if node == goal:
            print("Goal Found!!!!!")
            print("Solution Path:", path)
            pathcost = calcpathcost(path)
            print("Path Cost:", pathcost)
            exit("done")

        if node not in expanded:
            expanded.append(node)

            neighbors = graph[node]
            for n in neighbors:
                if n not in expanded:
                    fringe.append(n)
                    new_path = list(path)
                    new_path.append(n)
                    pathq.append(new_path)

    print("Goal not found")
    exit("done")

graph = {'a': ['b', 'c'], 'b': ['c', 'd', 'e'], 'c': ['d', 'e'], 'd': ['g'], 'e': ['d', 'g']}
cost = {'ab': 5, 'ac': 2, 'bc': 6, 'bd': 2, 'be': 8, 'cd': 7, 'ce': 6, 'dg': 6, 'ed': 5, 'eg': 4}
start = 'a'
goal = 'g'
expanded = []
fringe = [start]
pathq = [start]
DFS()
