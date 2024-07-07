import sys

def calcpathcost(path):
    pathcost = 0
    for i in range(1, len(path)):
        edge = path[i - 1] + path[i]
        stepcost = cost[edge]
        pathcost = pathcost + stepcost
    return pathcost

def DLS_limit(node, path, limit):
    if node == goal:
        print("Goal Found!!!!!")
        print("Solution Path:", path)
        pathcost = calcpathcost(path)
        print("Path Cost:", pathcost)
        sys.exit("done")
    elif limit == 0:
        return
    else:
        neighbours = graph[node]
        for n in neighbours:
            if n not in path:
                new_path = list(path)
                new_path.append(n)
                expanded.append(node)
                DLS_limit(n, new_path, limit - 1)

def DLS(limit):
    while fringe:
        node = fringe.pop(0)
        path = pathq.pop(0)
        DLS_limit(node, path, limit)

graph = {'a': ['b', 'c'], 'b': ['c', 'd', 'e'], 'c': ['d', 'e'], 'd': ['g'], 'e': ['d', 'g']}
cost = {'ab': 5, 'ac': 2, 'bc': 6, 'bd': 2, 'be': 8, 'cd': 7, 'ce': 6, 'dg': 6, 'ed': 5, 'eg': 4}
start = 'a'
goal = 'h'  # Change the goal to a non-existent node to trigger the "Goal Not Found" message
expanded = []
fringe = [start]
pathq = [start]
DLS(3)
