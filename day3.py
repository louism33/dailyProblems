'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given the root to a binary tree, implement serialize(root), which serializes the tree into a string,
 and deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
'''
import re

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(node, offset="- "):
    newOffset = "-" + offset
    s = offset + str(node.val)
    l = ""
    r = ""
    if node.left != None:
        l = serialize(node.left, newOffset) + "\n"
    if node.right != None:
        r = "\n" + serialize(node.right, newOffset)
    return l + s + r

def deserialize(nodeString, offset="- "):
    newOffset = "-"+offset
    rootPattern = "^"+offset+"(.*)"
    currentRoot = re.search(rootPattern, nodeString, flags=re.MULTILINE)
    if currentRoot:
        root = currentRoot.group(1)
        splitPattern = "[\n]*^"+offset+"[^\n]*[\n]*"
        f = re.split(splitPattern, nodeString, flags=re.MULTILINE)
        left = deserialize(f[0], newOffset) if len(f[0]) > 0 else None
        right = deserialize(f[1], newOffset) if len(f[1]) > 0 else None
    else:
        return None
    return Node(root, left, right)


node = Node('root', Node('left', Node('left.left'), Node('left.right')), Node('right'))
n = Node("2222")

n2 = serialize(n)

n3 = deserialize(n2)
assert n3.val == n.val

assert deserialize(serialize(node)).left.left.val == 'left.left'
