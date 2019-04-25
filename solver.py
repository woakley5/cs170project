import networkx as nx
import random

def solve(client):
    client.end()
    client.start()
    print("Home: " + str(client.home))

    edges = list(nx.bfs_edges(client.G, source = client.home))
    edges.reverse()

    for e in edges:
        scoutResult = client.scout(e[1], list(range(1, client.students)))
        scoutValues = list(scoutResult.values())
        if scoutValues.count(True) >= len(scoutValues)/2:
            client.remote(e[1], e[0])
    print(client.bot_locations) 
    client.end()