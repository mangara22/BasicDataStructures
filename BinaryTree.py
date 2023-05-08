class BTNode:
    def __init__(self, data, left, right):
        self.left = left
        self.right = right
        self.data = data
        
    def getData(self):
        return self.data
    def getLeft(self):
        return self.left
    def getRight(self):
        return self.right
    
    def setData(self, newdata):
        self.data = newdata
    def setLeft(self, newleft):
        self.left = newleft
    def setRight(self, newright):
        self.right = newright
        
    def maxDepth(self):
        if self.left == None and self.right == None:
            return 1
        elif self.left == None:
            return 1 + self.right.maxDepth()
        elif self.right == None:
            return 1 + self.left.maxDepth()
        else:
            return 1 + max(self.left.maxDepth(), self.right.maxDepth())
    
    def inOrder(self, root):
        result = []
        if root:
            result = self.inOrder(root.getLeft())
            result.append(root.getData())
            result += self.inOrder(root.getRight())
        return result
    def preOrder(self, root):
        result = []
        if root:
            result.append(root.getData())
            result += self.preOrder(root.getLeft())
            result += self.preOrder(root.getRight())
        return result
    def postOrder(self, root):
        result = []
        if root:
            result += self.postOrder(root.getLeft())
            result += self.postOrder(root.getRight())
            result.append(root.getData())
        return result
    
    def getLeftMost(self):
        if self.left == None:
            return self.data
        else:
            return self.left.getLeftMost()
        
    def getRightMost(self):
        if self.right == None:
            return self.data
        else:
            return self.right.getRightMost()
        
    def __str__(self):
        result = ""
        result += "This binary tree has a depth of: " + str(self.maxDepth())
        result += "\nIn-Order traversal: " + str(self.inOrder(self))
        result += "\nPre-Order traversal: " + str(self.preOrder(self))
        result += "\nPost-Order traversal: " + str(self.postOrder(self))
        result += "\nLeftmost Node is: " + str(self.getLeftMost())
        result += "\nRightmost Node is: " + str(self.getRightMost())
        return result
        
if __name__ == '__main__':
    btree = BTNode(5, BTNode(3, BTNode(7, None, None), BTNode(8, None, None)), BTNode(10, BTNode(1, None, None), BTNode(9, None, None)))
    '''
                5
               / \
              3   10
             / \  / \
            7  8  1  9
    '''
    print(btree)