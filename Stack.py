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
        
class Stack:
    def __init__(self):
        self.front = None
        self.count = 0
        
    def push(self, item):
        self.front = Node(item, self.front)
        self.count+=1

    def pop(self):
        value = self.front.getData()
        self.front = self.front.getNext()
        self.count-=1
        return value
    
    def __str__(self):
        result = ""
        nodeptr = self.front
        for i in range(self.count):
            if i == 0:
                result += str(nodeptr.getData()) + " TOP\n"
            elif i == self.count-1:
                result += str(nodeptr.getData()) + " BOTTOM\n"
            else:
                result += "" + str(nodeptr.getData()) + "\n"
            nodeptr = nodeptr.getNext()
        result += str(self.count) + " elements in the stack"
        return result
                
if __name__ == '__main__':
    stack = Stack()
    for i in range(1, random.randint(2, 10)):
        stack.push(i)
    stack.pop()
    print(stack)