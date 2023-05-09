import random
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
        
    def __str__(self):
        return "Node's data is: " + str(self.data) + ", next Node is: " + str(self.next) + "\n"
        
class LinkedList:
    def __init__(self):
        self.head = Node(0, None)
        self.tail = self.head
        self.count = 0
        
    def add(self, thing):
        if self.head.getNext() == None:
            self.head.setNext(Node(thing, None))
            self.tail = self.head.getNext()
        else:
            self.tail.setNext(Node(thing, None))
            self.tail = self.tail.getNext()
        self.count+=1
            
    def __str__(self):
        print("There are " + str(self.count) + " elements in this LinkedList")
        result = ""
        nodeptr = self.head.getNext()
        for i in range(self.count):
            if(nodeptr.getNext() == None):
                result += nodeptr.getData()
            else:
                result += nodeptr.getData() + " -> "
            nodeptr = nodeptr.getNext()
        return result
    
if __name__ == '__main__':
    list = LinkedList()
    for i in range(1, random.randint(2, 15)):
        list.add(str(i))
    print(list)