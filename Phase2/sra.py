import sys

''' Create the vertex class and assigning the properties for each vertex by including the status like visited or not ,
 predecessor initially set to None and the adjacencieslist is empty list along with the minDistance of vertex set to infinity'''


class Vertex(object):
    ## This is the constructor that implements the class object
    def _init_(self, name):
        ## Assigning the name property
        self.name = name
        self.visited = False
        self.predecessor = None
        self.adjacenciesList = []
        self.minDistance = sys.maxsize  ## initialize min distance with infinity

        ## to help the priority queue to decide its vertex based on minDistances

    ## Here we implement the minheap using the priority queue data structure

    def _lt_(self, other):
        selfPriority = self.minDistance
        otherPriority = other.minDistance
        return selfPriority < otherPriority


class Edge(object):
    # creating an edge object with the edge's weight, starting node
    def _init_(self, weights, startVertex, targetVertex):
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
        str = ""
        while node != None:

            str += node.name + "-->"

            if node != None:
                node = node.predecessor;
        str += "You have Reached!"
        print(str)