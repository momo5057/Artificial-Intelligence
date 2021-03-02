
print "Warning, it will take forever to compile... sorry \n"
graph = {}
keyList = []
graphWeight = {}
heuristicWeight = {}
with open("heuristic.txt") as f:
    for line in f:
        (node, heuristic) = line.split()
        heuristicWeight[node] = heuristic

with open("edges.txt") as f:
    for line in f:
        (key, val, weight) = line.split()
        if keyList.count(int(key)) > 0:
            graph[key].append(val)
        else:
            graph.setdefault(key, [])
            graph[key].append(val)
            keyList.append(key)
        graphWeight[key, val] = weight
        if keyList.count(int(val)) > 0:
            graph[val].append(key)
        else:
            graph.setdefault(val, [])
            graph[val].append(key)
            keyList.append(val)
        graphWeight[val, key] = weight


def bfs(start, end):
    queue = []
    visited = set()
    nodesVisited = 0
    nodesInPath = 1
    pathWeight = 0.0
    # push the first path into the queue
    queue.append([start])
    while queue:
        # get the first path from the queue
        #print queue
        path = queue.pop(0)

        # get the last node from the path
        if isinstance(path, list):
            node = path[-1]
        else:
            path = [path]
            node = path[-1]
        # path found
        if node == end:
            nodesInPath = len(path)
            for i in range(len(path)-1):
                 step = path[i], path[i+1]
                 pathWeight += float(graphWeight[step])
            return "Num Nodes Visited: " + str(nodesVisited) + "\nNum nodes on path: " + str(nodesInPath) + "\nDistance (km): " + str(pathWeight)
        # enumerate all adjacent nodes, construct a new path and push it into the queue
        elif node not in visited:
            for adjacent in graph.get(node, []):
                if adjacent not in path:
                    if adjacent not in visited:
                        new_path = list(path)
                        new_path.append(adjacent)
                        queue.append(new_path)
                        nodesVisited+=1
            visited.add(node)
    print "No path found \n"

def ucs(start, end):
    queue = {}
    visited = set()
    nodesVisited = 1
    nodesInPath = 1
    minPathCost = float("inf")
    # push the first path into the queue
    queue[0] = start

    #new_path.append(adjacent)
    while queue:
        pathWeight = 0.0
        minValue = 0
        # make list of weights in this path
        for i in queue.keys():
            minValue = queue.keys()
        #find min weight in this path
        min = "inf"
        for i in minValue:
            if i < min:
                min = i
        #set this path to the queue with the smallest weight
        path = queue[min]
        #delete that queue
        del queue[min]
        #set node to the last node in the path
        if isinstance(path, list):
            node = path[-1]
        else:
            path = [path]
            node = path[-1]
        # path found
        if node == end:
            nodesInPath = len(path)
            for i in range(len(path)-1):
                 step = path[i], path[i+1]
                 pathWeight += float(graphWeight[step])
            return "Num Nodes Visited: " + str(nodesVisited) + "\nNum nodes on path: " + str(nodesInPath) + "\nDistance (km): " + str(pathWeight)
        # enumerate all adjacent nodes, construct a new path and push it into the queue
        elif node not in visited:
            for adjacent in graph.get(node, []):
                pathWeight = 0
                if adjacent not in path:
                    if adjacent not in visited:
                        #get total weight of this path
                        for i in range(len(path)-1):
                             step = path[i], path[i+1]
                             pathWeight += float(graphWeight[step])
                        pathWeight += float(graphWeight[node, adjacent])
                        #put the extended path onto the queue
                        new_path = list(path)
                        new_path.append(adjacent)
                        queue[pathWeight] = new_path
                        nodesVisited+=1
            visited.add(node)
    #if queue empty with no answer
    return "No path found \n"

def astar(start, end):
    queue = {}
    visited = set()
    nodesVisited = 1
    nodesInPath = 1
    minPathCost = float("inf")
    # push the first path into the queue
    queue[0] = start

    #new_path.append(adjacent)
    while queue:
        pathWeight = 0.0
        minValue = 0
        # make list of weights in this path
        for i in queue.keys():
            minValue = queue.keys()
        #find min weight in this path
        min = "inf"
        for i in minValue:
            if i < min:
                min = i
        #set this path to the queue with the smallest weight
        path = queue[min]
        #delete that queue
        del queue[min]
        #set node to the last node in the path
        if isinstance(path, list):
            node = path[-1]
        else:
            path = [path]
            node = path[-1]
        # path found
        if node == end:
            nodesInPath = len(path)
            for i in range(len(path)-1):
                 step = path[i], path[i+1]
                 pathWeight += float(graphWeight[step])
                 #pathWeight += float(heuristicWeight[path[i]])
            return "Num Nodes Visited: " + str(nodesVisited) + "\nNum nodes on path: " + str(nodesInPath) + "\nDistance (km): " + str(pathWeight)
        # enumerate all adjacent nodes, construct a new path and push it into the queue
        elif node not in visited:
            for adjacent in graph.get(node, []):
                pathWeight = 0
                if adjacent not in path:
                    if adjacent not in visited:
                        #get total weight of this path
                        for i in range(len(path)-1):
                             step = path[i], path[i+1]
                             pathWeight += float(graphWeight[step])
                             pathWeight += float(heuristicWeight[path[i]])
                        pathWeight += float(graphWeight[node, adjacent])
                        pathWeight += float(heuristicWeight[adjacent])
                        #put the extended path onto the queue
                        new_path = list(path)
                        new_path.append(adjacent)
                        queue[pathWeight] = new_path
                        nodesVisited+=1
            visited.add(node)
    #if queue empty with no answer
    return "No path found \n"


print "Breath first search"
print bfs('104779422', '105012740')
print "\nUniform Cost Search"
print ucs('104779422', '105012740')
print "\nAStar Search"
print astar('104779422', '105012740')
#Print notes visited, Nodes in path, distance of path
