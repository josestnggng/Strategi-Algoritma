"""
Author : Jose Alfredo Sitanggang

Graph Algorithm
- List Adjacency
- DFS (Depth First Search) regular loop and recursive
- BFS (Breadth First Search) regular loop and recursive
- Print Graph
"""


from collections import deque

class Graph:

    def __init__(self, V):
        self.V = V
        self.adj = [None]*V
        for i in range(self.V):
            self.adj[i] = list()

    def add_edge(self, src, dst):
        self.adj[src].append(dst)
        self.adj[dst].append(src)

    def DFS(self, src):
        visited = set()

        print(src, end=" ")
        visited.add(src)
        # init stack with src child
        stack = self.adj[src].copy()

        # we can use len(stack)>0
        # but, len(visited)=V -> all vertex has visited
        # and we don't care stack empty or not
        while len(visited) < self.V:
            top = stack.pop()
            # if top has visited keep going
            if top not in visited:
                print(top, end=" ")
                visited.add(top)
                # get all child nodes of the `top` then
                # push to the stack if each node has not visited
                adj_top = self.adj[top]
                for node in adj_top:
                    if node not in visited:
                        stack.append(node)
        print("")

    def BFS(self, src):
        visited = set()

        print(src, end=" ")
        visited.add(src)
        # init queue with src child
        queue = deque(self.adj[src])

        while len(queue) > 0:
            first = queue.popleft()
            if first not in visited:
                print(first, end=" ")
                visited.add(first)
                # get all child nodes of the `top` then
                # push to the stack if each node has not visited
                adj_first = self.adj[first]
                for node in adj_first:
                    if node not in visited:
                        queue.append(node)
        print("")

    # Recursive Approach
    def DFSR(self, node, visited):
        if len(visited) == self.V:
            return
        print(node, end=" ")
        visited.add(node)
        for v in self.adj[node]:
            if v not in visited:
                self.DFSR(v, visited)

    def DFS_recursive(self, src):
        visited = set()
        self.DFSR(src, visited)
        print("")

    def BFSR(self, src, visited, queue):
        if len(visited) == self.V:
            return

        if src not in visited:
            print(src, end=" ")
            visited.add(src)
            for node in self.adj[src]:
                if node not in visited:
                    queue.append(node)
                    first = queue.popleft()
                    self.BFSR(first, visited, queue)

    def BFS_recursive(self, src):
        visited = set()
        queue = deque(self.adj[src])
        self.BFSR(src, visited, queue)
        print("")

    # utility
    def print_graph(self):
        for i in range(self.V):
            print("Adj of node {0}".format(i), end="")
            for adj in self.adj[i]:
                print("->{0}".format(adj), end="")
            print("\n")


if __name__ == "__main__":
    V = 5
    graph = Graph(V)
    graph.add_edge(0, 1)
    graph.add_edge(0, 4)
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(1, 4)
    graph.add_edge(2, 3)
    graph.add_edge(3, 4)
    # graph.print_graph()
    graph.DFS(0)
    graph.DFS_recursive(0)
    graph.BFS(0)
    graph.BFS_recursive(0)
