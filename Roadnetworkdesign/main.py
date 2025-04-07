import matplotlib.pyplot as plt
import networkx as nx

class DisjointSet:
    def __init__(self):
        self.parent = {}

    def make_set(self, item):
        self.parent[item] = item

    def find(self, item):
        if self.parent[item] != item:
            self.parent[item] = self.find(self.parent[item])
        return self.parent[item]

    def union(self, set1, set2):
        root1 = self.find(set1)
        root2 = self.find(set2)
        if root1 != root2:
            self.parent[root2] = root1

def kruskal_mst(vertices, edges, ds):
    mst = []
    total_cost = 0
    edges.sort(key=lambda x: x[2])

    for u, v, weight in edges:
        if ds.find(u) != ds.find(v):
            ds.union(u, v)
            mst.append((u, v, weight))
            total_cost += weight

    return mst, total_cost

def visualize_graph(vertices, edges, mst_edges):
    G = nx.Graph()

    for vertex in vertices:
        G.add_node(vertex)

    for u, v, w in edges:
        G.add_edge(u, v, weight=w, color='gray')

    for u, v, w in mst_edges:
        G[u][v]['color'] = 'green'

    pos = nx.spring_layout(G)
    colors = [G[u][v]['color'] for u, v in G.edges]
    labels 4 nx.get_edge_attributes(G, 'weight')

    nx.draw(G, pos, with_labels=True, edge_color=colors, node_color='lightblue', node_size=500, font_size=10)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.title("Minimum Spanning Tree using Kruskal's Algorithm")
    plt.show()

def main():
    vertices = []
    n = int(input("Enter number of cities: "))
    for i in range(n):
        city = input(f"Enter name of city {i+1}: ")
        vertices.append(city)

    e = int(input("Enter number of roads (edges): "))
    edges = []
    print("\nEnter road details (city1 city2 cost):")
    for _ in range(e):
        u, v, w = input().split()
        edges.append((u, v, int(w)))

    ds = DisjointSet()
    for city in vertices:
        ds.make_set(city)

    mst_edges, total_cost = kruskal_mst(vertices, edges, ds)

    print("\nSelected roads in MST:")
    for u, v, w in mst_edges:
        print(f"{u} - {v} : {w}")
    print("Total Cost of MST:", total_cost)

    visualize_graph(vertices, edges, mst_edges)

if __name__ == "__main__":
    main()
