__author__ = 'bilge'
import numpy as np
import networkx as nx
import sys
G = nx.Graph()



def unique_number_of_colors(colors):
    _n = set()
    for n, c in colors.items():
        _n.add(c)
    return len(_n)


def find_best_candidate(graph, colored):
    if True: #optimised
        candidates_with_values = [
            (
            -len({colored[neigh] for neigh in graph[n] if neigh     in colored}),
            -len({neigh          for neigh in graph[n] if neigh not in colored}),
            n
            ) for n in graph if n not in colored]
        candidates_with_values.sort()
        candidates = [n for a,b,n in candidates_with_values]
    if candidates:
        candidate = candidates[0]
        return candidate
    return None

nb_calls = 0

def solve(graph, colors, colored, depth):
    global nb_calls
    nb_calls += 1
    n = find_best_candidate(graph, colored)
    if n is None:
        return colored # Solution found
    for c in colors - {colored[neigh] for neigh in graph[n] if neigh in colored}:
        colored[n] = c
        if solve(graph, colors, colored, depth+1):
            return colored
        else:
            del colored[n]
    return None

#instance 1 : 6
#instance 2 : 20
#instance 3 : 17
#instance 4 : 90
#instance 5 : 16

with open(sys.argv[1]) as f:
    color_num = 16
    node = np.uint16(0)
    edge = np.uint16(0)
    best = np.uint16(0)
    node, edge = map(np.uint16, f.readline().split(sep=" "))
    data = [list(map(np.uint64, line.split(sep=" "))) for line in f]
    for i in range(edge):
        G.add_edge(data[i][0],data[i][1])
    colors = {i for i in range(color_num)}
    new_colors = solve(G, colors, dict(), 0)
    print(unique_number_of_colors(new_colors))
    for i,key in new_colors.items():
        print(key, end=" ")