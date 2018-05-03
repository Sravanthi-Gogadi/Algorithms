import sys

''' Create the vertex class and assigning the properties for each vertex by including the status like visited or not ,
 predecessor initially set to None and the adjacencieslist is empty list along with the minDistance of vertex set to infinity'''
class Vertex(object):
    
    def __init__(self,name):
	## Assigning the name property
        self.name= name
        self.visited = False
        self.predecessor = None
        self.adjacenciesList = []
        self.minDistance = sys.maxsize ## initialize min distance with infinity
		
	# Function that defines on what basis we select a minimum Node: "minimum Distance"
    # Required to tell the Heap that which node is the minimum Node and that is the Root
    # Orders the nodes according to Minimum Distance before adding to the Heap.
    # A Node is selected if the distance between Current Node and Node to be reached is smaller than other Nodes.

    # Step where we check for smallest weight in Heap Content and select it for next step
     
    ## to help the priority queue to decide its vertex based on minDistances
	## Here we implement the minheap using the priority queue data structure
	# Less than method to define on what basis a minimum Node is selected
    
    def __lt__(self, other):
        
        selfPriority=self.minDistance
        otherPriority=other.minDistance
        return selfPriority<otherPriority
		
    
    #creating an edge object with the edge's weight, start vertex and end vertex  
class Edge(object):
    def __init__(self, weights, startVertex, targetVertex):
        self.weights=weights
        self.startVertex=startVertex
        self.targetVertex= targetVertex

	# Import Heap Functions to get the Min. Heap Root Value
import heapq 
      
    # Dijkastra Algorithm Implementation  
class Algorithm(object):    

	# Function to Calculate the Shortest Path
    # Requires List of Vertices.

    def calculateShortestPath(self, vertexList, startVertex):
        queue=[]		# Implementing Heap using 1-D array
        startVertex.minDistance = 0;       # The min Distance of the starting vertex is "0".
        heapq.heappush(queue, startVertex)                   #initially, pushing the start vertex onto the Heap
    
        while len(queue)>0: # While the heap "queue" has items in it
			# Pop the item from heap, it pops the Root Node
            # Since, we use the lt functions to get only the minimum node,
            # so the minimum Node is Popped out of Heap.
            actualVertex = heapq.heappop(queue)
            for edge in actualVertex.adjacenciesList:          
                u = edge.startVertex
                v = edge.targetVertex
                newDistance=u.minDistance+ edge.weights      # Calculating weight
            
			
			 # Since, initially all Nodes except the start node have a weight of Infinity
             # Hence, weights will be updated based on new calculated minimum weights.
                if newDistance< v.minDistance:
                    v.predecessor = u
                    v.minDistance = newDistance
					# Update the Heap with new weights of each node
                    heapq.heappush(queue,v)
    
    
                
    def getShortestPathTo(self, targetVertex):
        # Target Vertex Node
        node = targetVertex
        return targetVertex.minDistance,node
    
    
    
        
    # Backtrack from the Target Node to the starting node using Predecessors
    def getPath(self, targetVertex):
        node = targetVertex
        str=""
        while node!=None:
                    
                    
                        
           
            str+=node.name+"-->"
              
            
            if node!=None:
                node=node.predecessor;
        str+="You have Reached!"				
        print(str)