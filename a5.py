class MaxHeap: 

    def __init__(self):
        self.size = 0 
        self.heap = [] 
        self.index_list = [] 

    def heapdown(self,i): # i is the index which has to be heaped down
        
        while (True):
            child1 = 2*i + 1 
            child2 = 2*i + 2
            if (child1 < len(self.heap)): 
                child = child1 
                if (child2 < self.size and self.heap[child2][0] > self.heap[child1][0]):
                    child = child2 
                if (self.heap[child][0] > self.heap[i][0]):
                    self.heap[i],self.heap[child] = self.heap[child],self.heap[i] 
                    self.index_list[self.heap[i][1]],self.index_list[self.heap[child][1]] = self.index_list[self.heap[child][1]],self.index_list[self.heap[i][1]]
                    i = child 
                else:return 

            else:
                return 

    def heapup(self,i): # i is the index to be heaped up 
        
        while (True) : 
            if (i <= 0):return 
            parent = (i - 1)//2 
            if (self.heap[i][0] > self.heap[parent][0]):
                self.heap[i],self.heap[parent] = self.heap[parent],self.heap[i] 
                self.index_list[self.heap[i][1]],self.index_list[self.heap[parent][1]] = self.index_list[self.heap[parent][1]],self.index_list[self.heap[i][1]] 
                i = parent 
            else:
                return 
    
    def buildheap(self,l): # l is a list to be converted to a maxheap 
        self.heap = l
        self.size = len(l) 
        self.index_list = [None] * self.size
        for i in range(self.size):
            self.index_list[l[i][1]] = i 
        for i in range(len(self.heap)-1 , -1,-1):
            self.heapdown(i) 
        return  
    
    def enqueue(self,key,value):
        
        self.heap.append((key,value)) 
        self.index_list[value] = self.size  
        self.size += 1 
        self.heapup(self.size-1)   
        return 

    def extract_max(self) : 
        l = self.heap
        l[0],l[-1] = l[-1],l[0]
        self.index_list[l[0][1]] = 0 
        node = l.pop() 
        self.index_list[node[1]] = None 
        self.size -= 1 
        self.heapdown(0)     
        return node  

    def change_key(self,old_key,new_key,value):
        index = self.index_list[value]  
        self.heap[index] = (new_key,value) 
        if (old_key > new_key) : 
            self.heapdown(index) 
            return
        if (old_key < new_key) : 
            self.heapup(index) 
            return 

class Graph: 
    def __init__(self,size) :
        self.n = size # n is the no. of vertices 
        self.m = 0 # no. of edges 
        self.adj = [0]*size
        for i in range(size):
            self.adj[i] = [i,[]] 
    
    def insert_edge(self,edge):
        self.m += 1 
        self.adj[edge[0]][-1].append(edge) 
        self.adj[edge[1]][-1].append(edge) 
        return 


def findMaxCapacity(n,links,s,t):
    graph = Graph(n) 
    # making the graph 
    for i in links:
        graph.insert_edge(i) 
    
    # making the priority queue 
    queue = MaxHeap()
    queue.heap  = [None] * n
    queue.index_list = [None] * n 
    queue.size = n 

    for i in range(n) :
        if ( i != s):  node = (0,i) 
        else : node = (float('inf'),i) 

        queue.heap[i] = node 
        queue.index_list[i] = i   
        

    d = [0] * n # list containing current capacities 
    d[s] = float('inf')  
    pre = [None] * n # list of predecessors 
    set = [] # list of vertices whose largest capacities have been determined 

    while (queue.size>0):
        node = queue.extract_max() 
        vertex = node[1] 
        if (vertex == t): set.append(node) ; break 
        else:
            set.append(node) 
            for edge in graph.adj[vertex][-1]:
                c =edge[2] 
                if (edge[0] == vertex) : u,v = edge[0],edge[1] 
                else : u,v = edge[1],edge[0] 
                
                
                     
                if ( (min(d[u],c)> d[v])): 
                    
                    pre[v] = u   
                    queue.change_key(d[v],min(d[u],c),v) 
                    d[v] = min(d[u],c) 
    # print(d) 
    # print(pre) 
    max_capacity = d[t] 
    path = [] 
    i = t; path.append(t) 
    while (pre[i] != s):
        path.append(pre[i]) ; i = pre[i] 
    path.append(s) 
    path.reverse() 
    return (max_capacity,path) 

#print(findMaxCapacity(3,[(0,1,1),(1,2,1)],0,1))
# print(findMaxCapacity(4,[(0,1,30),(0,3,10),(1,2,40),(2,3,50),(0,1,60),(1,3,50)],0,3))
#print(findMaxCapacity(4,[(0,1,30),(1,2,40),(2,3,50),(0,3,10)],0,3))
# print(findMaxCapacity(4,[(0,1,30),(0,3,10),(1,2,40),(2,3,50),(0,1,60),(1,3,50)],0,3))
#print(findMaxCapacity(5,[(0,1,3),(1,2,5),(2,3,2),(3,4,3),(4,0,8),(0,3,7),(1,3,4)],0,2))
#print(findMaxCapacity(7,[(0,1,2),(0,2,5),(1,3,4), (2,3,4),(3,4,6),(3,5,4),(2,6,1),(6,5,2)],0,5))