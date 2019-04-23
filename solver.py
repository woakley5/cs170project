import networkx as nx
import random
import matplotlib.pyplot as plt

def solve(client):
    client.end()
    client.start()

    edges = list(nx.dfs_edges(client.G, source = client.home))
    edges.reverse()

    # Vcolors = []
    # Ecolors = []
    # for n in client.G.nodes:
    #     if n == client.home:
    #         Vcolors.append(1.0)
    #     else:
    #         Vcolors.append(0.75)

    # for e in client.G.edges:
    #     Ecolors.append(0.12)

    
    # nx.draw(client.G, node_size = 20, node_color = Vcolors, edge_color = Ecolors)
    # plt.show()

    for e in edges:
        client.remote(e[1], e[0])

    client.end()
    

