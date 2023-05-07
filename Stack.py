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
    
    def top(self):
        if(self.front == None):
            return "Stack is empty!"
        return self.front.getData()
    
    def __str__(self):
        result = ""
        nodeptr = self.front
        for i in range(self.count):
            if i == 0:
                result += "TOP:    " + str(nodeptr.getData()) + "\n"
            elif i == self.count-1:
                result += "BOTTOM: " + str(nodeptr.getData())
            else:
                result += "MIDDLE: " + str(nodeptr.getData()) + "\n"
            nodeptr = nodeptr.getNext()
        return result
                
if __name__ == '__main__':
    stack = Stack()
    for i in range(9):
        stack.push(str(i))
    print(stack)