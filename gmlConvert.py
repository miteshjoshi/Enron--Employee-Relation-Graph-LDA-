
import networkx as nx
G = nx.Graph()

input = open ('path','r')

while True:
    s = input.readline()
    if not s: break
    a = s.split()[0]
    b = s.split()[1]
    c = s.split()[2]
    a = int(a)
    b = int(b)
    c = float(c)
    G.add_node(a)
    G.add_node(b)
    G.add_edge(a, b, c)
   
input.close()

nx.write_gml(G, 'outfile.gml')

