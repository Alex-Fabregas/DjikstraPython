import sys
import random
import timeit
import time


class Graph():
    # constructor
    def __init__(self, vertices):
        self.V = vertices
        self.matrix = [[0 for column in range(vertices)] for row in range(vertices)]

    # calculate the min distance in of the values still not yet found
    def min_distance(self, dist, pathset):
        min = sys.maxsize
        index = -1
        for x in range(self.V):
            if pathset[x] == False and dist[x] <= min:
                min = dist[x]
                index = x
        return index

    # for debugging, this method prints out the matrix
    def print_graph(self):
        for x in range(self.V):
            for y in range(self.V):
                if y < self.V - 1:
                    print(self.matrix[x][y], ",", end="")
                else:
                    print(self.matrix[x][y])

    # Typical print function for Dijkstra's algorithm, prints all of the connections from source
    def print_solution(self, dist):
        print("Vertex \t Distance from source: ")
        for x in range(self.V):
            if dist[
                x] == sys.maxsize:  # Our random matrix includes disconnected nodes, this is to fix the print function to compensate
                print("not connected to graph")
            else:
                print(str(x) + "\t\t" + str(dist[x]))

    # my implementation of Dijkstra's algorithm for adjacency matrices
    def dijkstra(graph, source):
        dist = []
        sptset = []
        for x in range(graph.V):
            dist.append(sys.maxsize)
            sptset.append(False)
        dist[source] = 0
        for count in range(graph.V):
            u = graph.min_distance(dist, sptset)
            sptset[u] = True
            for v in range(graph.V):
                if not sptset[v] and graph.matrix[u][v] != 0 and dist[u] != sys.maxsize and dist[u] + graph.matrix[u][
                    v] < dist[v]:
                    dist[v] = dist[u] + graph.matrix[u][v]
    # graph.print_solution(dist) #Remove the comment of this line to see the connections of the graph


# this function generates a randomized matrix of size * size
def large_matrix(size):
    graph = Graph(size)
    nodes = size
    for x in range(size):
        for y in range(size):
            graph.matrix[x][y] = 0
    while nodes > 0:
        x = random.randint(0, size - 1)
        y = random.randrange(0, size - 1)
        if x != y:
            nodes = nodes - 1
            graph.matrix[x][y] = graph.matrix[y][x] = random.randrange(0, 20)
    return graph


# test function, it outputs the dimension of the matrix and the time of the run. Set to 50 loops.
def test_function(name):
    for x in (10, 100, 1000, 5000, 10000, 15000, 20000):
        setup = "from __main__ import " + name
        if name == "Graph":
            setup += "\nfrom __main__ import large_matrix"
            test = '''
graph = large_matrix(''' + str(x) + ''')
for x in range(50):
    graph.dijkstra(0)'''
            num = 1
        else:
            test = name + "(1000)"
            num = 50
        print("The test for %d sized matrix took:  %f seconds to run" % (
        x, timeit.timeit(stmt=test, setup=setup, number=num)))
    return 0


# execution starts here
graph = Graph(1)
test_function(graph.__class__.__name__)
