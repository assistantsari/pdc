import networkx as nx
import numpy as np
import matplotlib.pyplot as plt


A = np.matrix(
    [
    [0,4,0,0,0,0,0,8,0],
    [4,0,8,0,0,0,0,11,0],
    [0,8,0,7,0,4,0,0,2],
    [0,0,7,0,9,14,0,0,0],
    [0,0,0,9,0,10,0,0,0],
    [0,0,4,14,10,0,2,0,0],
    [0,0,0,0,0,2,0,1,6],
    [8,11,0,0,0,0,1,0,7],
    [0,0,2,0,0,0,6,7,0]
    ]
)

G = nx.from_numpy_array(A)

node_labels = {i: chr(97 + i) for i in range(len(A))}  
G = nx.relabel_nodes(G, node_labels)

def draw_graph(G, title="Graph"):
    pos = nx.spring_layout(G)  
    plt.figure(figsize=(8, 6))
    nx.draw(G, pos, with_labels=True, node_color="lightblue", edge_color="gray", font_weight="bold")
    edge_labels = {(u, v): G[u][v]['weight'] for u, v in G.edges()}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.title(title)
    plt.show()

def prims_algorithm(G):
    MST = nx.Graph()  
    total_cost = 0

    start_node = list(G.nodes)[0]
    visited = set([start_node])
    
    edges = [
        (G[start_node][neighbor]['weight'], start_node, neighbor)
        for neighbor in G[start_node]
    ]
    
    while len(visited) < len(G.nodes):
        edges = sorted(edges, key=lambda x: x[0])  
        for weight, u, v in edges:
            if v not in visited:
                MST.add_edge(u, v, weight=weight)
                total_cost += weight
                visited.add(v)
                for neighbor in G[v]:
                    if neighbor not in visited:
                        edges.append((G[v][neighbor]['weight'], v, neighbor))
                break
    return MST, total_cost

draw_graph(G, title="Original Graph")

MST, total_distance = prims_algorithm(G)
draw_graph(MST, title=f"Minimum Spanning Tree (Total Weight: {total_distance})")

print(f"Total weight of the Minimum Spanning Tree: {total_distance}")
