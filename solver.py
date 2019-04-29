import networkx as nx
import random
import copy

def solve(client):
    client.end()
    client.start()

    # 91 Points versus 75 points

    print("Home: " + str(client.home))

    nonHomeNodes = list(client.G.nodes)
    nonHomeNodes.remove(client.home)

    heuristics = []
    students = list(range(1, client.students + 1))
    for n in nonHomeNodes:
        val = client.scout(n, students)
        yes = 0
        for s in val.values():
            if s:
                yes += 1
        heuristics.append((n, yes))

    heuristics.sort(key = lambda x: x[1], reverse = True)
    #print(heuristics)

    index = 0
    while len(client.bot_locations) < client.bots and index < len(heuristics):
        node = heuristics[index][0]
        path = nx.algorithms.shortest_path(client.G, source=node, target=client.home )
        for n in range(0, len(path) - 1):
            result = client.remote(path[n], path[n + 1])
            if result == 0:
                break
        index += 1

    # print("Node: " + str(node))
    # print("Home: " + str(client.home))
    # print(path)


    print(client.bot_locations)
    client.end()
