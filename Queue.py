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
        
class Queue:
    def __init__(self):
        self.count = 0
        self.front = None
        self.back = None
        
    def add(self, item):
        if(self.count == 0):
            self.front = Node(item, None)
            self.back = self.front
        else:
            self.back.setNext(Node(item, None))
            self.back = self.back.getNext()
        self.count+=1
        
    def remove(self):
        if(self.count == 0):
            print("Cannot remove from an empty queue!")
        else:
            value = self.front.getData()
            self.front = self.front.getNext()
            self.count-=1
            if(self.count == 0):
                self.back = None
            return value
        
    def __str__(self):
        result = ""
        nodeptr = self.front
        for i in range(self.count):
            if i == 0:
                result += str(nodeptr.getData()) + " FRONT\n"
            elif i == self.count-1:
                result += str(nodeptr.getData()) + " BACK\n"
            else:
                result += "" + str(nodeptr.getData()) + "\n"
            nodeptr = nodeptr.getNext()
        result += str(self.count) + " items in the queue"
        return result
    
if __name__ == '__main__':
    queue = Queue()
    for i in range(0, random.randint(2, 10)):
        queue.add(i)
    queue.remove()
    print(queue)