# hashTable
 Implement an in-place Hash Table ADT with the following methods. You are required to use an
array of tuples (key, value) as your structure to maintain your data. This means that your structure should be like H
= [[(k1, v1)], [(k2, v2)]…]). When collisions happens, your data structure should look like H = [[(k1, v1), (k2,v2)],
[(k3, v3)]…] (i.e., a multidimensional array).
a. H.put(k, v): Associates a value v with a key k by adding the tuple (k, v) to the array. If the key exists,
replaces it with the new value.
b. H.get(k): Returns the value v associated with key k in the Hash Table.
c. H.remove(k): Removes the tuple (k, v) from H. The method should return (k, v).
