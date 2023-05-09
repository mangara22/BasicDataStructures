class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next
        
    def getData(self):
        return self.data
    def getNext(self):
        return self.next
    
    def setData(self, newdata):
        self.data = newdata
    def setNext(self, newnext):
        self.next = newnext;
        
class HashTable:
    def __init__(self, size):
        self.numcount = 0
        self.size = size
        self.table = [None] * self.size
        
    def hash(self, item):
        item = str(item)
        hashcode = 0
        for i in range(len(item)):
            hashcode += ord(item[i]) * 3079
        return hashcode % self.size
    
    def add(self, element):
        index = self.hash(element)
        if self.table[index] == None:
            self.table[index] = Node(element, None)
        else:
            nodeptr = self.table[index]
            while(nodeptr.getNext() != None):
                if(nodeptr.getData() == element):
                    return None
                nodeptr = nodeptr.getNext()
            if(nodeptr.getData() == element):
                return None
            nodeptr.setNext(Node(element, None))
        self.numcount += 1
        
    def __str__(self):
        result = ""
        for i in range (self.size):
            result += "[" + str(i) + "]  : "
            hashptr = self.table[i]
            if hashptr == None:
                result += "NONE"
            else:
                while(hashptr != None):
                    if(hashptr.getNext() == None):
                        result += hashptr.getData()
                    else:
                        result += hashptr.getData() + "->"
                    hashptr = hashptr.getNext()
            result += "\n"
        result += "Number of elements in HashTable: " + str(self.numcount)
        result += "\nHashTable size: " + str(self.size)
        return result
    
if __name__ == '__main__':
    hashtable = HashTable(10)
    hashtable.add('hello')
    hashtable.add('test')
    hashtable.add('you')
    hashtable.add('laptop')
    hashtable.add('phone')
    hashtable.add('pop')
    hashtable.add('computer')
    hashtable.add('science')
    print(hashtable)