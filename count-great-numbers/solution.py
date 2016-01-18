import sys
import os
import functools
from random import randint
import timeit  


""" Binary Tree """

class Node:
    def __init__(self, val):
        self.l = None
        self.r = None
        self.v = val

class Tree:
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def add(self, val):
        if(self.root == None):
            self.root = Node(val)
        else:
            self._add(val, self.root)

    def _add(self, val, node):
        if(val < node.v):
            if(node.l != None):
                self._add(val, node.l)
            else:
                node.l = Node(val)
        else:
            if(node.r != None):
                self._add(val, node.r)
            else:
                node.r = Node(val)

    def find(self, val):
        if(self.root != None):
            return self._find(val, self.root)
        else:
            return None

    def _find(self, val, node):
        if(val == node.v):
            return node
        elif(val < node.v and node.l != None):
            self._find(val, node.l)
        elif(val > node.v and node.r != None):
            self._find(val, node.r)

    def deleteTree(self):
        # garbage collector will do this for us. 
        self.root = None

    def printTree(self):
        if(self.root != None):
            self._printTree(self.root)

    def _printTree(self, node):
        if(node != None):
            self._printTree(node.l)
            print str(node.v) + ' '
            self._printTree(node.r)

    def treeSize(self):
    	if self.root is None:
    		return 0

		if self.root is not None:
			return 1 + self.treeSize(self.root.left) + self.treeSize(self.root.right)

""" end Tree """


#_a = [3, 4, 1, 2, 4, 6]
#_b = [1, 2, 3, 4, 5, 6]

_a_cnt = 0
_a_cnt = int(input())
_a_i = 0
_a = []
while _a_i < _a_cnt:
	_a_item = randint(1, _a_cnt);
	_a.append(_a_item)
	_a_i += 1

_b_cnt = 0
_b_cnt = int(input())
_b_i = 0
_b = []
while _b_i < _b_cnt:
	_b_item = randint(1, _a_cnt-1);
	_b.append(_b_item)
	_b_i += 1

#print(_a)
#print(_b)

def countGreaterNumbers():	
	a_sorted = list(_a)
	a_sorted.sort()

	res = []

	for i in range(0, len(_b)-1):
		
		base_idx = _b[i]
		base_val = _a[base_idx-1]

		#print('_b['+str(i)+']: '+ str(base_idx) + ' -> ' + str(base_val))

		filtered_list = list(filter(lambda x: x > base_val, _a))

		res.append(len(filtered_list))
		
	print(res)
    
if __name__ == '__main__':
    import timeit
    tree = Tree()

    for n in _a:
    	tree.add(n)

    #tree.add(3)
    #tree.add(4)
    #tree.add(0)
    #tree.add(8)
    #tree.add(2)
    tree.printTree()
    #print (tree.find(3)).v
    #print tree.find(8)
    #tree.deleteTree()
    #tree.printTree()  

    #print(timeit.timeit("countGreaterNumbers()", setup="from __main__ import countGreaterNumbers", number=1))  