import networkx as nx
import random

def solve(client):
    client.end()
    client.start()
    print("Home: " + str(client.home))
    
    edges = list(nx.bfs_edges(client.G, source = client.home))
    edges.reverse()

    index = 0
    while len(client.bot_locations) != client.bots and index < len(edges):
        e = edges[index]
        client.remote(e[1], e[0])
        index += 1

    if len(client.bot_locations) != client.bots:
        print("index ran out")
    else:
        print("Found all bots!")
        print(client.bot_locations)

    client.end()