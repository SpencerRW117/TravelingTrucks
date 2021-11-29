#Defines a single element that can be stored in the hash table with a key value pair. 
class HashTableElement:
    def __init__(self, key, val):
        self.key = key
        self.val = val
#Defines the hash table with list chaining along with insert, modify, search, and remove functions. 
class HashContainer:
    #Constructor
    def __init__(self, size=10):
        self.table= []
        #Sets an empty list in each index of the main list. This creates the adjacency list representation of the graph, a list of lists.
        for i in range(size):
            self.table.append([])
    
    
    #Inserts a record into the hash container. 
    def insert(self, key, val):
        bucket_index = hash(key) % len(self.table)
        bucket = self.table[bucket_index]

        for el in bucket:
            if el[0] == key:
                el[1] = val
                return True
        
        new_bucket_element = [key, val]
        bucket.append(new_bucket_element)
        return True

    #Updates a record in the has table.     
    def modify(self, key, val):
        bucket_index = hash(key) % len(self.table)
        bucket = self.table[bucket_index]
        for el in bucket:
            if el[0] == key:
                el[1] = val
                return True
    
    #Returns a record in the has table with matching key. 
    def search(self, key):
        bucket_index = hash(key) % len(self.table)
        bucket = self.table[bucket_index]
        for el in bucket:
            if el[0] == key:
                return el[1]
        return None
    #Removes a record from the hash table with matching key. 
    def remove(self, key):
        bucket_index = hash(key) % len(self.table)
        bucket = self.table[bucket_index]
        for el in bucket:
            if el[0] == key:
                bucket.remove([el[0], el[1]])
    

        
        
    




