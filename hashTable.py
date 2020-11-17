class HashTable:
    def __init__(self,N,P):
        self.size = N
        self.H = [None] * self.size
        self.setMap()
        self.probing = P

    def setMap(self):
        for i in range(self.size):
            self.H[i] = []

    def hashFunction(self,key):
        index = key % self.size
        return index

    #Get new indexPosition for tuple
    def linear(self, index):
        #Check for Collision in hash Map
        if len(self.H[index]) == 0:
            print("I am in base case")
            return index
        else:
            nextIndex = (index+1)%self.size
            return self.linear(nextIndex)

    def quadratic(self, index):
        j = 0
        newIndex = index
        while(len(self.H[newIndex]) != 0):
            newIndex = (index + j*j) % self.size
            j += 1
        return newIndex

    def doubleHashing(self, index, key):
        j = 0
        newIndex = index
        secondHash = 7 - key % 7
        while(len(self.H[newIndex]) != 0):
            newIndex = (index + (j * secondHash) % self.size)
            j += 1
        return newIndex
        
        

    def put(self,k,v):
        
        #Check if key exist
        for arr in self.H:
            if arr == None:
                continue
            else:
                for tup in arr:
                    if tup[0] == k:
                        tup = (k,v)
        
        #Get the index for the new tuple
        index = self.hashFunction(k)

        #Resolve collision using probing
    
        if self.probing == "l":
            newIndex = self.linear(index)
            
        elif self.probing == "q":
            newIndex = self.quadratic(index)
            
        elif self.probing == "d" :
            newIndex = self.doubleHashing(index,k)
            
        else:
            print("Please enter type of probing correctly. For example l for linear, q for quadratic, and d for double hashing.")
            return

        
        
        #Append the tuple to the array in the specified index
        arr = self.H[newIndex]
        arr.append((k,v))
        
        
        
    def get(self, k):
        #Get Value
        for arr in self.H:
            if arr == None:
                continue
            else:
                for tup in arr:
                    if tup[0] == k:
                        return tup[1]
                    
    def remove(self,k):
        #Given k, remove and return (k,v)
        for arr in self.H:
            if arr == None:
                continue
            else:
                for tup in arr:
                    if tup[0] == k:
                        tempTup = tup
                        arr.remove(tup)
                        return tempTup
                        
                
    def print(self):
        for item in self.H:
            print (item, end=" ")
        print()
        print()


#Main Code 
h = HashTable(4," ")
h.put(0,200)
h.put(4,200)
h.put(101,222)
#h.put(4,600)
#h.put(5,300)
h.print()




        
