# Linked Lists: It is basically a collection of nodes, where node is an object 
#                 in a node you store data and the address of another node.

# Advantages:
#     1) Write operations are very fast eg: insertion and deletion and have time complexity of constant i.e O(1)
#     2) Can be used to create other data structures eg: stack, queues, doubly linkedlist etc

#-------------------------------------------------------------------------------------------------

class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class LinkedList:

    def __init__(self):

        # Empty Link List:
        self.head = None
        # No. of nodes in LL
        self.n = 0

    def __len__(self):
        return self.n
    
    def insert_head(self, value):

        # create a new Node 
        new_node  = Node(value)

        # create connection
        new_node.next = self.head

        # reassign head 
        self.head = new_node

        # increment node count 
        self.n = self.n + 1

    def traverse(self):
        curr = self.head 
        while curr != None:
            print(curr.data)
            curr = curr.next

    def append(self, value):
        curr = self.head

        # create a new Node 
        new_node = Node(value)

        if curr ==  None:
            self.head = new_node
            self.n = self.n + 1
            return

        while curr.next != None:
            curr = curr.next

        # assign new nodes address to tail
        curr.next = new_node

        # increment the node count
        self.n = self.n + 1

    def traverse_last_second_last_element(self):
        curr = self.head

        # this will traverse a Lined List to  second last element 
        while curr.next != None:
            print(curr.data)
            curr = curr.next
        
        print("::::::::::::::::::::::::::::")

        curr = self.head
        # this will traverse a Lined List to last element 
        while curr != None:
            print(curr.data)
            curr = curr.next

    def insert_after(self, after, value):

        new_node = Node(value)

        curr = self.head

        while curr != None:
            if curr.data == after:
                break
            curr = curr.next

        if curr != None:
            new_node.next = curr.next
            curr.next = new_node
            self.n = self.n + 1
        else:
            return "item not found"

    def clear(self):
        self.head = None
        self.n = 0

    def delete_head(self):
        if self.head == None:
            return 'Empty List'
        self.head = self.head.next

    def pop(self):
        curr = self.head
        if curr == None:
            return 'Empty List'
        if curr.next == None:
            return self.delete_head()
        while curr.next.next != None:
            curr = curr.next

        curr.next = None
        self.n = self.n - 1

    def remove(self, value):
        if self.head == None:
            return 'Empty Linked List'
        if self.head.data == value:
            return self.delete_head()
        curr = self.head
        while curr.next != None:
            if curr.next.data == value:
                break
            curr = curr.next
        
        if curr.next == None:
            return 'Item not found'
        else:
            curr.next = curr.next.next
            self.n = self.n - 1

    def search(self, value):
        pos = 0 
        curr = self.head
        while curr != None:
            if curr.data == value:
                return pos
            curr = curr.next
            pos = pos + 1
        return 'Not Found'

    def __getitem__(self, index):
        curr = self.head
        pos = 0 
        while curr != None:
            if pos == index:
                return curr.data
            pos = pos + 1
            curr = curr.next
        return 'IndexEror'

    def replace_max(self, value):
        temp = self.head
        max = temp

        while temp != None:
            if max.data < temp.data:
                max = temp.data

            temp = temp.next
        max.data = value

    def sum_of_odd_index(self):
        curr = self.head
        pos = 0 
        sum  = 0
        while curr != None:
            if pos % 2 != 0:
                sum = curr.data + sum
            pos = pos + 1
            curr = curr.next
        return sum

l = LinkedList()
# print(len(l))
l.insert_head(100)
l.insert_head(200)
l.insert_head(300)
l.insert_head(400)

# print(len(l))
# l.append(747)
# l.traverse()
# l.traverse_last_second_last_element()
# print(l.insert_after(355500, 999))

# l.clear()
# l.traverse()
# l.delete_head()
# l.traverse()
# l.pop()
# l.traverse()
# l.remove(300)
# l.traverse()
# print(l.search(100))
# print(l[200])
# l.replace_max(999999)
# l.traverse()
print(l.sum_of_odd_index())




