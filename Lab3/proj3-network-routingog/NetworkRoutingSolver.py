#!/usr/bin/python3
import sys

from CS312Graph import *
import time


class NetworkRoutingSolver:
    def __init__( self, display ):
        pass



    def initializeNetwork( self, network ):
        assert( type(network) == CS312Graph )
        self.network = network


    def getShortestPath( self, destIndex ):
        self.dest = destIndex
        print(destIndex)

        # TODO: RETURN THE SHORTEST PATH FOR destIndex
        #       INSTEAD OF THE DUMMY SET OF EDGES BELOW
        #       IT'S JUST AN EXAMPLE OF THE FORMAT YOU'LL 
        #       NEED TO USE

        path_edges = []
        total_length = 0

        print(len(self.network.nodes))
        node = self.network.nodes[self.source]
        edges_left = 3

        while edges_left > 0:
            edge = node.neighbors[2]
            path_edges.append( (edge.src.loc, edge.dest.loc, '{:.0f}'.format(edge.length)) )
            total_length += edge.length

            node = edge.dest
            edges_left -= 1

        return {'cost':total_length, 'path':path_edges}



    def computeShortestPaths( self, srcIndex, use_heap=False ):
        if(use_heap):
            heap = Heap(self.network.nodes)
        else:
            unsorted = Unsorted(self.network.nodes)

        print(srcIndex)
        for i in range(len(self.network.nodes)):
            print(self.network.nodes[i])

        self.source = srcIndex-1

        t1 = time.time()
        # TODO: RUN DIJKSTRA'S TO DETERMINE SHORTEST PATHS.
        #       ALSO, STORE THE RESULTS FOR THE SUBSEQUENT
        #       CALL TO getShortestPath(dest_index)

        t2 = time.time()

        return (t2-t1)


class Unsorted:
    def __init__(self, nodes):
        self.prevList = []
        self.distList = []
        self.nodes = []
        for i in range(len(nodes)):
            self.nodes.append(nodes[i].node_id)
            self.prevList.append(None)
            self.distList.append(sys.maxsize)

    def makeQueue(self):
        return True

    def deleteMin(self):
        return True

    def decreaseKey(self):
        return True


class Heap:
    def __init__( self, nodes ):
        self.nodes = nodes

    def makeQueue(self):
        return True

    def deleteMin(self):
        return True

    def decreaseKey(self):
        return True
