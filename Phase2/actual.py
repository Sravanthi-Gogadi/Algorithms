from sra import Vertex
from sra import Edge
from sra import Algorithm

node1 = Vertex("64110")
node2 = Vertex("64111")
node3 = Vertex("64112")
node4 = Vertex("64113")
node5 = Vertex("64114")
node6 = Vertex("64115")
node7 = Vertex("64116")
node8 = Vertex("64117")
node9 = Vertex("64118")

edge1 = Edge(2, node1, node2)
edge2 = Edge(3, node1, node3)
edge3 = Edge(5, node1, node4)
edge4 = Edge(4, node2, node3)
edge5 = Edge(7, node2, node5)
edge6 = Edge(6, node4, node5)
edge7 = Edge(8, node5, node6)
edge8 = Edge(2, node5, node7)
edge9 = Edge(5, node5, node8)
edge10 = Edge(2, node6, node7)
edge11 = Edge(6, node7, node9)

typ = input("Enter Type of vehicle required 1. Fire 2. Ambulance 3. Police \n")
availability_list = [
    [{"type": 1, "zipcode": node1, "availability": 0}, {"type": 2, "zipcode": node1, "availability": 1},
     {"type": 3, "zipcode": node1, "availability": 0}],
    [{"type": 1, "zipcode": node2, "availability": 0}, {"type": 2, "zipcode": node2, "availability": 1},
     {"type": 3, "zipcode": node2, "availability": 1}],
    [{"type": 1, "zipcode": node3, "availability": 0}, {"type": 2, "zipcode": node3, "availability": 1},
     {"type": 3, "zipcode": node3, "availability": 1}],
    [{"type": 1, "zipcode": node4, "availability": 0}, {"type": 2, "zipcode": node4, "availability": 2},
     {"type": 3, "zipcode": node4, "availability": 1}],
    [{"type": 1, "zipcode": node5, "availability": 0}, {"type": 2, "zipcode": node5, "availability": 2},
     {"type": 3, "zipcode": node5, "availability": 0}],
    [{"type": 1, "zipcode": node6, "availability": 0}, {"type": 2, "zipcode": node6, "availability": 2},
     {"type": 3, "zipcode": node6, "availability": 1}],
    [{"type": 1, "zipcode": node7, "availability": 0}, {"type": 2, "zipcode": node7, "availability": 2},
     {"type": 3, "zipcode": node7, "availability": 1}],
    [{"type": 1, "zipcode": node8, "availability": 1}, {"type": 2, "zipcode": node8, "availability": 2},
     {"type": 3, "zipcode": node8, "availability": 1}],
    [{"type": 1, "zipcode": node8, "availability": 1}, {"type": 2, "zipcode": node8, "availability": 2},
     {"type": 3, "zipcode": node8, "availability": 1}]]
all = []
allnodes = [node1, node2, node3, node4, node5, node6, node7, node8, node9]
### check for the availability of the requested type of the vehicle
for v in availability_list:
    ##print(v)
    for x in v:

        if x['type'] == int(typ) and x['availability'] > 0:
            x['availability'] = x['availability'] - 1  #### refer your doubt in availability

            all.append(x['zipcode'])
##print(all)

node1.adjacenciesList.append(edge1)
node1.adjacenciesList.append(edge2)
node1.adjacenciesList.append(edge3)
node2.adjacenciesList.append(edge4)
node2.adjacenciesList.append(edge5)
node4.adjacenciesList.append(edge6)
node5.adjacenciesList.append(edge7)
node5.adjacenciesList.append(edge8)
node5.adjacenciesList.append(edge9)
node6.adjacenciesList.append(edge10)
node7.adjacenciesList.append(edge11)

al = Algorithm()
zip = input("Enter the zipcode:\n")

dic = {"64110": node1, "64111": node2, "64112": node3, "64113": node4, "64114": node5, "64115": node6, "64116": node7,
       "64117": node8, "64118": node9}

for i in dic.keys():
    if i == zip:
        al.calculateShortestPath(allnodes, dic[i])

dis = []
for i in all:
    dis.append(al.getShortestPathTo(i))

dis.sort(key=lambda tup: tup[0])
print("The available node is at a distance of {} miles from {}".format(dis[0][0], dis[0][1].name))
req = dis[0][1]

al.getPath(req)