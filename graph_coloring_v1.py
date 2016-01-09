from networkx.algorithms.coloring import greedy_coloring

__author__ = 'bilge'
import numpy as np
import networkx as nx
import itertools

G = nx.Graph()

def findBestCandidate(G):
    counter = 0
    temp=0
    best = 0
    for n,nbrs in G.adjacency_iter():
        for nbr in nbrs.items():
            temp += 1
        if counter < temp:
            counter = temp
            best = n
        temp=0
    return best

def checkNeighbours(G):
    colors = {}  # dictionary to keep track of the colors of the nodes
    nodes = G.nodes()
    for node in nodes:
         # set to keep track of colors of neighbours
        neighbour_colors = set()

        for neighbour in G.neighbors_iter(node):
            if neighbour in colors:
                neighbour_colors.add(colors[neighbour])

        for color in itertools.count():
            if color not in neighbour_colors:
                break

         # assign the node the newly found color
        colors[node] = color
    return colors

def unique_number_of_Colors(colors):
    _n = set()
    for n, c in colors.items():
        _n.add(c)
    return len(_n)

with open("data/gc_70_7") as f:
    node = np.uint16(0)
    edge = np.uint16(0)
    best = np.uint16(0)
    node, edge = map(np.uint16, f.readline().split(sep=" "))
    data = [list(map(np.uint64, line.split(sep=" "))) for line in f]
    for i in range(edge):
        G.add_edge(data[i][0],data[i][1])
    colors = checkNeighbours(G)
    print(unique_number_of_Colors(colors))
    for i,key in colors.items():
        print(key, end=" ")
