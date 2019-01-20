'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

An XOR linked list is a more memory efficient doubly linked list.
Instead of each node holding next and prev fields, it holds a field named both,
 which is an XOR of the next node and the previous node.
 Implement an XOR linked list; it has an add(element) which adds the element
 to the end, and a get(index) which returns the node at index.

If using a language that has no pointers (such as Python),
you can assume you have access to get_pointer and dereference_pointer
functions that converts between nodes and memory addresses.
'''

def get_pointer(obj):
    return 1

class Node:
    def __init__(self, val, index, previous):
        self.val = val
        self.index = index
        self.both = previous

    def add_next(self, next):
        self.both = self.calc_both(self.both, next)

    def calc_both(self, previous, next):
        return previous ^ next

    def get_next_node(self, previous):
        return self.both ^ previous

class XorLinkedList:
    def __init__(self):
        self.first_node = None

    def add(self, value):
        if self.first_node is None:
            self.first_node = Node(value, 0, None)
        else:
            last_node = self.get_final_node()
            new_node = Node(value, last_node.index + 1, last_node)
            last_node.add_next(new_node)

    def get_final_node(self):
        node1 = self.first_node
        node2 = self.first_node.get_next_node()
        while node2 is not None:
            node1 = node2
            node2 = node2.get_next_node()
        return node1


a = XorLinkedList()