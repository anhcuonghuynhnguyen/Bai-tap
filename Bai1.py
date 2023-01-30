from collections import defaultdict

# BFS and DFS


class Graph:
    # Constructor
    def __init__(self):
        # default dictionary to store graph
        self.graph = defaultdict(list)

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # Function to print a BFS of graph
    def BFS(self, s):
        # Mark all the vertices as not visited
        visited = []
        # Create a queue for BFS
        queue = []
        # Mark the source node as visited and enqueue it
        visited.append(s)
        queue.append(s)
        while queue:
            # Dequeue a vertex from queue and print it
            s = queue.pop(0)
            print(s, end=" ")
            # Get all adjacent vertices of the dequeued vertex s. If a adjacent has not been visited, then mark it visited and enqueue it
            for neighbour in self.graph[s]:
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)

    # A function used by DFS
    def DFSUtil(self, v, visited):
        # Mark the current node as visited and print it
        visited.add(v)
        print(v, end=' ')
        # Recur for all the vertices adjacent to this vertex
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.DFSUtil(neighbour, visited)

    # The function to do DFS traversal. It uses recursive DFSUtil()
    def DFS(self, v):
        # Create a set to store visited vertices
        visited = set()
        # Call the recursive helper function to print DFS traversal
        self.DFSUtil(v, visited)

    # A function used by DLS
    def DLSUtil(self, v, visited, ll, cl, g):
        # Mark the current node as visited and print it
        visited.add(v)
        if v == g:
            print(v)
            return True
        print(v, end='-')
        # Recur for all the vertices adjacent to this vertex
        cl += 1
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                if cl > ll:
                    continue
                if self.DLSUtil(neighbour, visited, ll, cl, g):
                    return True
        return False

    # The function to do DLS traversal. It uses recursive DLLUtil()
    def DLS(self, v, ll, g):
        # Create a set to store visited vertices
        visited = set()
        # Call the recursive helper function to print DLS traversal
        self.DLSUtil(v, visited, ll, 0, g)

    # A function used by IDS
    def IDSUtil(self, v, visited, ll, cl, g):
        # Mark the current node as visited and print it
        visited.add(v)
        if v == g:
            print(v)
            return True
        print(v, end=' ')
        # Recur for all the vertices adjacent to this vertex
        cl += 1
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                if cl > ll:
                    continue
                if self.IDSUtil(neighbour, visited, ll, cl, g):
                    return True
        return False

    # The function to do IDS traversal. It uses recursive DLLUtil()
    def IDS(self, v, g):
        # Create a set to store visited vertices
        visited = set()
        # Call the recursive helper function to print IDS traversal
        ll = 1
        check = self.IDSUtil(v, visited, ll, 0, g)
        while not check:
            print("Giới hạn bậc", ll, "thất bại")
            visited = set()
            ll += 1
            check = self.IDSUtil(v, visited, ll, 0, g)
        print("Giới hạn bậc", ll, "thành công")


# UCS
def uniform_cost_search(goal, start, graph, cost):
    # minimum cost upto goal state from starting
    answer = []

    # create a priority queue
    queue = []

    # set the answer vector to max value
    for i in range(len(goal)):
        answer.append(10**8)

    # insert the starting index
    queue.append([0, start])

    # map to store visited node
    visited = {}

    # count
    count = 0

    # while the queue is not empty
    while (len(queue) > 0):

        # get the top element of the
        queue = sorted(queue)
        p = queue[-1]

        # pop the element
        del queue[-1]

        # get the original value
        p[0] *= -1

        # check if the element is part of
        # the goal list
        if (p[1] in goal):

            # get the position
            index = goal.index(p[1])

            # if a new goal is reached
            if (answer[index] == 10**8):
                count += 1

            # if the cost is less
            if (answer[index] > p[0]):
                answer[index] = p[0]

            # pop the element
            del queue[-1]

            queue = sorted(queue)
            if (count == len(goal)):
                return answer

        # check for the non visited nodes
        # which are adjacent to present node
        if (p[1] not in visited):
            for i in range(len(graph[p[1]])):

                # value is multiplied by -1 so that
                # least priority is at the top
                queue.append(
                    [(p[0] + cost[(p[1], graph[p[1]][i])]) * -1, graph[p[1]][i]])

        # mark as visited
        visited[p[1]] = 1

    return answer


def ImplementBFSandDFSandDLS():
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)

    print("Following is BFS (starting from vertex 2)")
    g.BFS(2)

    print("\nFollowing is DFS (starting from vertex 2)")
    g.DFS(2)


def ImplementUCS():
    # create the graph
    graph, cost = [[] for i in range(8)], {}

    # add edge
    graph[0].append(1)
    graph[0].append(3)
    graph[3].append(1)
    graph[3].append(6)
    graph[3].append(4)
    graph[1].append(6)
    graph[4].append(2)
    graph[4].append(5)
    graph[2].append(1)
    graph[5].append(2)
    graph[5].append(6)
    graph[6].append(4)

    # add the cost
    cost[(0, 1)] = 2
    cost[(0, 3)] = 5
    cost[(1, 6)] = 1
    cost[(3, 1)] = 5
    cost[(3, 6)] = 6
    cost[(3, 4)] = 2
    cost[(2, 1)] = 4
    cost[(4, 2)] = 4
    cost[(4, 5)] = 3
    cost[(5, 2)] = 6
    cost[(5, 6)] = 3
    cost[(6, 4)] = 7

    # goal state
    goal = []

    # set the goal
    # there can be multiple goal states
    goal.append(5)

    # get the answer
    answer = uniform_cost_search(goal, 0, graph, cost)

    # print the answer
    print("\nFollowing is UCS")
    print("Minimum cost from 0 to {0} is = ".format(goal), answer[0])


def ImplementationDLSandIDS():
    gdls = Graph()
    gdls.addEdge(1, 2)
    gdls.addEdge(1, 3)
    gdls.addEdge(2, 4)
    gdls.addEdge(2, 5)
    gdls.addEdge(4, 6)

    print("\nFollowing is DLS (starting from vertex 1 and ending at 5, limit level is 2)")
    gdls.DLS(1, 2, 5)
    print("\nFollowing is IDS (starting from vertex 1 and ending at 6)")
    gdls.IDS(1, 6)


ImplementBFSandDFSandDLS()
ImplementUCS()
ImplementationDLSandIDS()
