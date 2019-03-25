

class WGraph:

    def __init__(self, V):
        self.V = V
        self.adj = [list() for i in range(self.V)]

    def add_edge(self, src, dst, w):
        self.adj[src].append({dst: w})
        self.adj[dst].append({src: w})

    def print_graph(self):

        for i in range(self.V):
            adj = self.adj[i]
            print("Vertex {0} adj to :".format(i))
            for node in adj:
                # each node have a dst,w pair
                k, v = node.popitem()
                print("\t{0} with weight {1}".format(k, v))

        print("\n")


if __name__ == "__main__":
    V = 5
    wgraph = WGraph(V)
    wgraph.add_edge(0, 1, 10)
    wgraph.add_edge(0, 4, 20)
    wgraph.add_edge(1, 2, 30)
    wgraph.add_edge(1, 3, 40)
    wgraph.add_edge(1, 4, 50)
    wgraph.add_edge(2, 3, 60)
    wgraph.add_edge(3, 4, 70)
    wgraph.print_graph()

    print("Contoh git commit")
