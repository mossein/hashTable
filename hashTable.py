class HashTable:
    def __init__(self,N):
        self.size = N
        #self.probing = probing
        self.H = [[None]] * self.size

    def put(self,k,v):
        if self.H[k-1] is not None:
            self.H[k-1] = []
            self.H[k-1].append((k,v))
        else:
            self.H[k-1] = []
            self.H[k-1].append((k,v))

    def get(self, k):
        if(k > self.size):
            print()
            print("Cannot check key: Key does not exist")
            return

        #Check if array in that position is == to none
        elif self.H[k-1] is None:
            print("404, Not Found!")
        
        else:
            for arr in self.H:
                for tup in arr:
                    #Check if tuple inside the array is equal to None
                    if tup == None:
                        continue
                    elif tup[0] == k:
                        return print(tup[1])
                


    def remove(self,k):
        if(k > self.size):
            print()
            print("Cannot remove key: Key does not exist")
            return

        #Check if array in that position is == to none
        elif self.H[k-1] is None:
            print("404, Not Found!")
        
        else:
            for arr in self.H:
                #i is position of tup
                for i in range(len(arr)):
                    #arr[i] is the tup
                    if arr[i][0] == k:
                        arr[i] = None
                    elif arr[i] == None:
                        continue
                        
                


        



          
    def printt(self):
        for item in self.H:
            print (item, end=" ")
        print()


#Main Code 
h = HashTable(4)
h.put(1,200)
h.put(3,400)
h.put(4,400)
h.put(2,400)
h.remove(3)
h.printt()
#h.get(1)
print()


        
