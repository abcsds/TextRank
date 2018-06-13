import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
import re
import networkx as nx
import editdistance


with open("hp.txt") as fp:
    text = fp.read().lower()
    words = word_tokenize(text)
    sentences = sent_tokenize(text)
    sentences = [re.sub('"', '', line) for line in sentences]

sim = editdistance.eval

def create_graph(sentences):
    G=nx.Graph()
    for i, sentence in enumerate(sentences):
        try:
            a,b = sentence,sentences[i+1]
            G.add_edge(a,b,weight=sim(a,b))
        except IndexError:
            pass
    return G


import matplotlib.pyplot as plt
G = create_graph(sentences=sentences)
pos=nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, node_size=700)
nx.draw_networkx_edges(G, pos)
plt.axis('off')
plt.savefig("weighted_graph.png") # save as png
plt.show()


pr = nx.pagerank(G)
sorted(pr[0])
