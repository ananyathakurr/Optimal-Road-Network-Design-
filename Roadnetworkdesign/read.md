#  Optimal Road Network Design using Kruskal’s Algorithm

This project helps in designing the most cost-efficient road network between cities using **Minimum Spanning Tree (MST)** concepts. We apply **Kruskal’s Algorithm** to select roads with the least construction cost while ensuring that all cities are connected without forming any loops.

##  Objective

To build an optimal (minimum cost) network of roads that connects all the given cities. The goal is to avoid redundant paths and minimize the total infrastructure cost.

##  What This Project Does

- Takes user input: cities, roads, and their construction costs.
- Constructs a graph with cities as nodes and roads as weighted edges.
- Applies **Kruskal's Algorithm** to compute the Minimum Spanning Tree.
- Displays selected roads and total cost.
- Visualizes the final road network with a graph (using `matplotlib` & `networkx`).

##  Algorithm Used

We use the **Greedy approach** of Kruskal's Algorithm:
- Sort all roads by increasing cost.
- Pick the lowest cost road that connects two different sets of cities.
- Use **Disjoint Set Union (Union-Find)** to avoid cycles in the network.

##  Technologies Used

- Python
- NetworkX (for graph structures)
- Matplotlib (for visualization)
- Disjoint Set Data Structure (custom implementation)



