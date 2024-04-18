# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 09:55:25 2024

@author: KLMoring

"""

import sys

class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}
        self.color = 'white'
        self.dist = sys.maxsize  # Initialize distance to infinity
        self.pred = None
        self.disc = 0
        self.fin = 0
    
    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight

    def setColor(self, color):
        self.color = color

    def setDistance(self, d):
        self.dist = d

    def setPred(self, p):
        self.pred = p

    def setDiscovery(self, dtime):
        self.disc = dtime
        
    def setFinish(self, ftime):
        self.fin = ftime
        
    def getFinish(self):
        return self.fin
        
    def getDiscovery(self):
        return self.disc
        
    def getPred(self):
        return self.pred
        
    def getDistance(self):
        return self.dist
        
    def getColor(self):
        return self.color

    def getConnections(self):
        return self.connectedTo.keys()
        
    def getWeight(self, nbr):
        return self.connectedTo[nbr]

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getId(self):
        return self.id

class Graph:
    def __init__(self):
        self.vertList = {}

    def addVertex(self, key):
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self, key):
        return self.vertList.get(key, None)

    def addEdge(self, fromVertex, toVertex, weight=0):
        if fromVertex not in self.vertList:
            self.addVertex(fromVertex)
        if  toVertex not in self.vertList:
            self.addVertex(toVertex)
        self.vertList[fromVertex].addNeighbor(self.vertList[toVertex], weight)

    def getVertices(self):
        return self.vertList.values()

    def dijkstra(self, startVertex):
        startVertex.setDistance(0)  # Set distance to source vertex to 0
        visited = set()  # Set to keep track of visited vertices
        queue = [startVertex]  # Initialize queue with start vertex

        while queue:
            currentVertex = queue.pop(0)
            visited.add(currentVertex)

            for nextVertex in currentVertex.getConnections():
                if nextVertex not in visited:
                    newDist = currentVertex.getDistance() + currentVertex.getWeight(nextVertex)
                    if newDist < nextVertex.getDistance():
                        nextVertex.setDistance(newDist)
                        nextVertex.setPred(currentVertex)
                        queue.append(nextVertex)

# Example usage of the Graph class
graph = Graph()

# Add vertices and edges
graph.addEdge(1, 2, 4)
graph.addEdge(1, 3, 11)
graph.addEdge(1, 4, 7)
graph.addEdge(2, 3, 8)
graph.addEdge(2, 4, 6) 
graph.addEdge(3, 5, 8)
graph.addEdge(3, 6, 7) 
graph.addEdge(4, 5, 9)
graph.addEdge(4, 6, 11)
graph.addEdge(6, 7, 6)
graph.addEdge(5, 7, 5)     

# Get the start vertex (e.g., vertex 1)
startVertex = graph.getVertex(1)

# Run Dijkstra's algorithm from the start vertex
graph.dijkstra(startVertex)

# Print shortest distances from the start vertex to all other vertices
for vertex in graph.getVertices():
    print("Shortest distance from New London to vertex", vertex.getId(), ":", vertex.getDistance())
