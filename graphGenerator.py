#Use G(n,p) to randomly generate around 100 graphs (presented in adjacency matrix). There are two factors at this current stage: number of nodes, number of edges. Assuming all the edges weigh the same.

import networkx as nx
import pandas as pd
import numpy as np

# Define the number of nodes and the probability
num_nodes = 5
prob = 0.5

# A list to hold the adjacency matrices
adj_matrices = []

# Generate 10 random graphs and their adjacency matrices
for _ in range(10):
    G = nx.gnp_random_graph(num_nodes, prob)
    adj_matrix = nx.adjacency_matrix(G).todense()  # Converts sparse matrix to dense
    adj_matrices.append(adj_matrix)

# Convert the adjacency matrices to pandas DataFrames
df_list = [pd.DataFrame(np.array(matrix)) for matrix in adj_matrices]

# Create a new Excel writer object
writer = pd.ExcelWriter('graph_adjacency_matrices.xlsx')

# Write each DataFrame to a separate sheet in the Excel file
for i, df in enumerate(df_list):
    df.to_excel(writer, sheet_name=f'Graph_{i+1}')

# Save the Excel file
writer.save()
