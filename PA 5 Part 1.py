# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 09:27:49 2024

@author: KLMoring
"""

ROOT = 0
LEFT_CHILD = 1
RIGHT_CHILD = 2

def binaryTree(rootVal):
    return [rootVal, [], []]
    
def insertLeft(root,newChild):
    # Pop off the old left child
    #print('root = ',root)
    oldChild = root.pop(LEFT_CHILD)
    #print('old child was ',oldChild)
    # Insert the new child
    root.insert(LEFT_CHILD,binaryTree(newChild))
    #print('root with new child inserted =',root)
    # Make the old child a child of the new child
    root[LEFT_CHILD][LEFT_CHILD] = oldChild
    #print('now also with old child as child of new child ',root)
    return root

def insertRight(root, newChild):
    oldChild = root.pop(RIGHT_CHILD)
    root.insert(RIGHT_CHILD,binaryTree(newChild))
    root[RIGHT_CHILD][RIGHT_CHILD] = oldChild
    return root    

def getRootVal(root):
    return root[ROOT]
    
def setRootVal(root, newVal):
    root[ROOT] = newVal

def getLeftChild(root):
    return root[LEFT_CHILD]

def getRightChild(root):
    return root[RIGHT_CHILD]

def printTree(tree,indent=''):
    print(indent,tree[ROOT])
    print()
    leftChild = getLeftChild(tree)
    if len(leftChild) > 1:
        indent += '   '
        printTree(leftChild,indent)
    rightChild = getRightChild(tree)
    if len(rightChild) > 1:
        indent += '   '
        printTree(rightChild,indent)

r = binaryTree(5)
insertRight(r,13)
insertRight(r,7)
r1 = getRightChild(r)
insertLeft(r1,6)
r3 = getRightChild(r1)
insertRight(r3,17) 
insertLeft(r3,11) 
r4 = getLeftChild(r3)
insertRight(r4,15)
insertLeft(r,1)
insertLeft(r,2)
l1 = getLeftChild(r)
insertRight(l1,3)
r2 = getRightChild(l1)
insertRight(r2,4)
print(f'The final binary search tree is:\n{r}')


