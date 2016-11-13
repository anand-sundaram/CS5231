import graph_tool.all as gt
graph1 = gt.load_graph("Torch_Malware.graphml")
graph2 = gt.load_graph("Torch.graphml")


print "Are the graphs isomorphic: ", gt.isomorphism(graph1, graph2)

similarEdgeNumber = gt.similarity(graph1, graph2, None, None, False)

# Gives number of edges with the same source vertex and same target vertex in both the graphs

similarityNorm = gt.similarity(graph1, graph2, None, None, True)

# The normalized value of similarity, calculated as the total number of similar edges divided by the total number of edges. 
# It is a rough measure of similarity, with 1 indicating a perfect match, and 0 indicating no match

print "Number of Similar Edges: ", similarEdgeNumber

print "Total Number of Edges: ", similarEdgeNumber/similarityNorm

print "Percentage similarity of Edges: ", similarityNorm

