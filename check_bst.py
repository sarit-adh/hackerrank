#https://www.hackerrank.com/challenges/ctci-is-binary-search-tree

""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

def checkBST(root):
    
    nodes = traverse(root)
    
    #if inorder traversal returns a list in which elements are strictly arranged in ascending order, it is binary search tree
    for i in range(1,len(nodes)):
        if (nodes[i-1] >= nodes[i]):
            return False
    
    return True



def traverse(root):
    
    #perform inorder traversal of the tree
    if root:
        return traverse(root.left) + [root.data] + traverse(root.right)
    return []
