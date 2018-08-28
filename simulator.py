
import networkx as nx
import matplotlib.pyplot as plt
import argparse
from random import choices
import numpy as np
from random import randint

__author__ = 'Pelin Icer Baykal'

'''
Epidemics simulator for transmission network

'''

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Simulates epidemics with power-law network')
    parser.add_argument("-n", metavar = "N", type = int, help='define number of vertices')

    args = parser.parse_args()
    N=args.n
    #print(N)

    #create a graph with degrees and a power law distribution
    s = nx.utils.powerlaw_sequence(N,2)
    #return a random graph with given expected degrees
    G = nx.expected_degree_graph(s, selfloops=False)

    #nodes of original graph
    original_nodes = list(G.nodes())

    #get the largest connected subgraph component
    Gc = max(nx.connected_component_subgraphs(G), key=len)

    # nodes of the subgraph
    subgraph_nodes = list(Gc.nodes())

    print("number of nodes: " , len(Gc))
    print("nodes: " , Gc.nodes())
    print("edges: " , Gc.edges())

    # isolated nodes
    isolates = list(nx.isolates(G))
    # G.remove_nodes_from(isolates)
    print("isolates: ", isolates)

    #degree distribution of the network
    degrees = [val for (node, val) in Gc.degree()]
    sumOfdeg=sum(degrees)
    for i in range(len(degrees)):
        #print(degrees[i])
        #print("sum" , sumOfdeg)
        degrees[i] = (degrees[i]/sumOfdeg)*100
    print("degree distribution " , degrees)

    #choose random nodes
    r = randint(1, len(Gc))
    #print(r)
    infected_patients = np.random.choice(list(Gc.nodes()), r , replace = False)
    print("random nodes: " , infected_patients )

    #draw and show graph
    pos2 = nx.spring_layout(Gc)
    pos1 = nx.spring_layout(G)


    f1 = plt.figure(1)
    f1.suptitle('Original Graph')
    nx.draw_networkx(G, pos1, node_color = 'b')

    f2 = plt.figure(2)
    f2.suptitle("Biggest connected subgraph")

    color_map = []
    for n in subgraph_nodes:
        #print(n)
        if n in infected_patients:
            color_map.append('r')
        else:
            color_map.append('b')

    nx.draw_networkx(Gc, pos1, node_color = color_map)

    nn = []
    for m in infected_patients:
        neighbor = list(G.neighbors(m))
        neighbors_ip = []
        for p in neighbor:
            if p not in infected_patients:
                neighbors_ip.append(p)
        print(m, " nodes neighbors: " , neighbors_ip)
        if not neighbors_ip:
            nn.append(neighbors_ip)
            print(nn)

    plt.show()


