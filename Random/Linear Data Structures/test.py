
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.nodes = 0

    def inser_head(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.nodes = self.nodes + 1

    def len(self):
        return self.nodes
    
    def traverse(self):
        curr = self.head
        while curr != None:
            print(curr.data)
            curr = curr.next

L = LinkedList()
L.inser_head(100)
L.inser_head(200)
L.inser_head(300)
print(L.len())
L.traverse()