import networkx as nx
import pandas as pd
import numpy as np

# Define the number of nodes and the probability
num_node = 5
prob = 0.5

# A list to hold the adjacency arrays
adj_arrays = []

# Generate 10 random graphs and their adjacency arrays
for _ in range(100):
    G = nx.gnp_random_graph(num_node, prob)
    adj_array = nx.adjacency_matrix(G).todense().tolist()  # Converts matrix to 2D array
    adj_arrays.append(adj_array)
    print(f'Graph_{_+1}:', adj_array)

# Convert the adjacency arrays to string representation
adj_arrays_str = ["\n".join(map(str, arr)) for arr in adj_arrays]

# Convert the adjacency array strings to a pandas DataFrame
df = pd.DataFrame(adj_arrays_str)

# Create a new Excel writer object
writer = pd.ExcelWriter('result.xlsx')

# Write DataFrame to the Excel file
df.to_excel(writer)

# Save the Excel file
writer.save()
