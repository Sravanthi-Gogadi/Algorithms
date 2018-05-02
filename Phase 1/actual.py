import djisktra
from djisktra import Vertex
from djisktra import Edge
from djisktra import Algorithm

## passing it to the 
node1 = Vertex("64110")
node2 = Vertex("64111")
node3 = Vertex("64112")
node4 = Vertex("64113")
node5 = Vertex("64114")

edge1=Edge(2,node1,node2)
edge2=Edge(3,node1,node3)
edge3=Edge(5,node1,node4)
edge4=Edge(4,node2,node3)
edge5=Edge(7,node2,node5)
edge6=Edge(6,node4,node5)

''''req_vehicletype=input("Enter the vehicle u need")
req_zipcode=input("Enter the zipcode")'''

availability_list=[{"type": 1,"zipcode": node1, "availability":0} , {"type": 2,"zipcode": node1, "availability":1}, {"type": 3,"zipcode": node1, "availability":0},
{"type": 1,"zipcode": node2, "availability":0} , {"type": 2,"zipcode": node2, "availability":1}, {"type": 3,"zipcode": node2, "availability":1},
{"type": 1,"zipcode": node3, "availability":0} , {"type": 2,"zipcode": node3, "availability":1}, {"type": 3,"zipcode": node3, "availability":1},
{"type": 1,"zipcode": node4, "availability":2} , {"type": 2,"zipcode": node4, "availability":2}, {"type": 3,"zipcode": node4, "availability":1},
{"type": 1,"zipcode": node5, "availability":1} , {"type": 2,"zipcode": node5, "availability":2}, {"type": 3,"zipcode": node5, "availability":0}]
all=[]

### check for the availability of the requested type of the vehicle
for x in availability_list:
    if x['type'] == 1 and x['availability']>0:
        x['availability'] = x['availability']-1
        all.append(x['zipcode'])
        print(x['zipcode'])
print(all)

node1.adjacenciesList.append(edge1)
node1.adjacenciesList.append(edge2)
node1.adjacenciesList.append(edge3)
node2.adjacenciesList.append(edge4)
node2.adjacenciesList.append(edge5)
node4.adjacenciesList.append(edge6)


##vertexList={node1,node2,node3,node4,node5}
al=Algorithm()
al.calculateShortestPath(all,Vertex("64110"))
#3nod=Vertex("64110")
##nod=Vertex(node5)
#al.getShortestPathTo(nod)
#al.getShortestPathTo(node1)


##s=list(map(str,all))
##print(s)

dis=[]
for i in all:
    
   
    dis.append(al.getShortestPathTo(i))
    
dis.sort(key=lambda tup: tup[0], reverse=True) 

req=dis[0][1]
##print(req)
al.getPath(req)

    














