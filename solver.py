import networkx as nx
import random

def solve(client):
    client.end()
    client.start()

    edges = list(nx.dfs_edges(client.G, source = client.home))
    edges.reverse()

    for e in edges:
        client.remote(e[1], e[0])
        
    client.end()