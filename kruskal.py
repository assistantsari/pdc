import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

A = np.matrix(
    [
        [0,4,0,1,0,0,0,0,0,0],
        [4,0,4,4,0,0,0,0,0,10],
        [0,4,0,0,2,1,0,0,0,0],
        [1,4,0,0,0,0,0,5,0,6],
        [0,0,2,0,0,0,2,0,0,0],
        [0,0,1,0,0,0,3,0,5,0],
        [0,0,0,0,2,3,0,0,3,4],
        [0,0,0,5,0,0,0,0,0,2],
        [0,0,0,0,0,5,3,0,0,3],
        [0,10,0,6,0,0,4,2,3,0]
    ]
)

G = nx.from_numpy_array(A)

labels = {i: chr(65 + i) for i in range(len(A))}  

def draw_graph(G, title):
    plt.figure(figsize=(8, 6))
    pos = nx.spring_layout(G)  
    nx.draw(G, pos, labels=labels, with_labels=True, node_color="lightblue", edge_color="gray", node_size=700, font_size=10)
    
    edge_labels = {(u, v): G[u][v]['weight'] for u, v in G.edges}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10)

    plt.title(title)
    plt.show()

draw_graph(G, "Original Graph with Labels A-J")

MST = nx.minimum_spanning_tree(G, algorithm="kruskal")

total_weight = sum(MST[u][v]['weight'] for u, v in MST.edges)

draw_graph(MST, f"Kruskal's MST (Total Weight: {total_weight})")

print(f"Total weight of the Minimum Spanning Tree (MST): {total_weight}")
