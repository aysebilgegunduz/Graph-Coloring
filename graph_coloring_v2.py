__author__ = 'bilge'
import numpy as np
import networkx as nx
import itertools

G = nx.Graph()

def check_valid(graph):
    for node,nexts in graph.adjacency_iter():
        assert(node not in nexts) # # no node linked to itself
        for next in nexts:
            assert(next in graph and node in graph[next]) # A linked to B implies B linked to A

def find_best_candidate(graph, guesses):
    if True: #optimised
        candidates_with_add_info = [
            (
            -len({guesses[neigh] for neigh in graph[n] if neigh     in guesses}),
            -len({neigh          for neigh in graph[n] if neigh not in guesses}),
            n
            ) for n in graph if n not in guesses]
        candidates_with_add_info.sort()
        candidates = [n for _,_,n in candidates_with_add_info]
    else:
        candidates = [n for n in graph if n not in guesses]
        candidates.sort() # just to have some consistent performances
    if candidates:
        candidate = candidates[0]
        assert(candidate not in guesses)
        return candidate
    return None

nb_calls = 0

def solve(graph, colors, guesses, depth):
    global nb_calls
    nb_calls += 1
    n = find_best_candidate(graph, guesses)
    if n is None:
        return guesses # Solution is found
    for c in colors - {guesses[neigh] for neigh in graph[n] if neigh in guesses}:
        assert(n not in guesses)
        assert(all((neigh not in guesses or guesses[neigh] != c) for neigh in graph[n]))
        guesses[n] = c
        indent = '  '*depth #bunu kapattım
        if solve(graph, colors, guesses, depth+1):
            print("%sGave color %s to %s" % (indent,c,n))
            return guesses
        else:
            del guesses[n]
    return None


def solve_problem(graph, colors):
    check_valid(graph)
    solution = solve(graph, colors, dict(), 0)
    #print(solution)
    #check_solution(graph,solution)
    return solution

def unique_number_of_Colors(colors):
    _n = set()
    for n, c in colors.items():
        _n.add(c)
    return len(_n)

with open("data/gc_50_1") as f:
    node = np.uint16(0)
    edge = np.uint16(0)
    best = np.uint16(0)
    node, edge = map(np.uint16, f.readline().split(sep=" "))
    data = [list(map(np.uint64, line.split(sep=" "))) for line in f]
    for i in range(edge):
        G.add_edge(data[i][0],data[i][1])
    colors = {i for i in range(90)}
    new_colors = solve_problem(G, colors)
    print(unique_number_of_Colors(new_colors))
    for i,key in new_colors.items():
        print(key, end=" ")