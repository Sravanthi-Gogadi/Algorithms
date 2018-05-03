import sys


class Vertex(object):
    def __init__(self, name):
        self.name = name
        self.visited = False
        self.predecessor = None
        self.adjacenciesList = []
        self.minDistance = sys.maxsize  ## initialize min distance with infinity

    ## to help the priority queue to decide its vertex based on minDistance
    def __cmp__(self, otherVertex):
        return self.cmp(self.minDistance, otherVertex.minDistance)

    def __lt__(self, other):
        selfPriority = self.minDistance
        otherPriority = other.minDistance
        return selfPriority < otherPriority


class Edge(object):
    def __init__(self, weights, startVertex, targetVertex):
        self.weights = weights
        self.startVertex = startVertex
        self.targetVertex = targetVertex


import heapq


class Algorithm(object):
    def calculateShortestPath(self, vertexList, startVertex):
        queue = []
        startVertex.minDistance = 0;
        heapq.heappush(queue, startVertex)

        while len(queue) > 0:
            actualVertex = heapq.heappop(queue)
            for edge in actualVertex.adjacenciesList:
                u = edge.startVertex
                v = edge.targetVertex
                newDistance = u.minDistance + edge.weights

                if newDistance < v.minDistance:
                    v.predecessor = u
                    v.minDistance = newDistance
                    heapq.heappush(queue, v)

    def getShortestPathTo(self, targetVertex):

        node = targetVertex
        return targetVertex.minDistance, node

    def getPath(self, targetVertex):
        node = targetVertex
        f = open('out.html', 'w')
        f.write("<p><img src="+"1.jpg"+"></p>")
        while node != None:

            f = open('out.html', 'a')
            f.write("<p><img src=" + "2.JPG" + "></p>")
            f.write("<span style="+"background-color:orange>"+ node.name +"</span><----")

            if node != None:
                node = node.predecessor;