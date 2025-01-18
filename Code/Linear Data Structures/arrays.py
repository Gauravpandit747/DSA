
# 1. Arrays :
#     Arrays are by default homogenious in nature, that means they can store only a value of only single Data type in them.
#     In order to make them heterogenious we use a concept called as refertial Arrays.

#     instead of using a regular call by value we use call by refrence, i.e instead of storing the values in continous assigned 
#     memory locations we store the address of new data in that memory location which is of int by default.

#     Example of referential arrays is Lists in Python 

#     Disadvantages of Referntial Arrays :
#     1) a Lill slower than the arrays in C
#     2) Requires extra memory 


#     Dynamic Array: 
#         Internally it is a Static array only.
#         Whenever a user requests to add a new element to a static array & the length of the static array is full.
#         A new array static array is created twice the length of previous static array and the older contents of prev. static 
#         aray are copied into new staic array, this process keeps on repeating as the static array keeps on filling.

#         Eg of Dynamic array is Python List

# https://pythontutor.com/


#------------------  Functionalities  Done  -------------------------------
# 1) create list 
# 2) len
# 3) append 
# 4) print
# 5) indexing 
# 6) pop 
# 7) clear
# 8) find
# 9) insert 
# 10) delete
# 11) remove

#------------------  Functionalities can be Done  -------------------------------
# 1) sor/min/max/sum
# 2) extend 
# 3) negative indexing 
# 4) slicing 
# 5) merge

#----------- Concept of Dynamic Array ------------------------
import sys
import ctypes

# L = []
# for i in range(100):
#     print(i,sys.getsizeof(L))
#     L.append(i)

# ---------------------------------------------------------------

class DynamicList:
    def __init__(self):
        self.size = 1
        self.n = 0
        # create a C type array with size == self.size
        self.A = self.__make_array(self.size)

    def __len__(self):
        return self.n

    def __str__(self):
        result = ""
        for i in range(self.n):
            result = result + str(self.A[i]) + ','

        return '[' + result[:-1] + ']'

    def __getitem__(self, index):
        if 0<= index < self.n:
            return self.A[index]
        else:
            return 'IndexError - Index out of range'

    def __delitem__(self, pos):
        if 0 <= pos < self.n:
            for i in range(pos, self.n-1):
                self.A[i] = self.A[i+1]

        self.n = self.n - 1

    def append(self, item):
        if self.size == self.n:
            # resize
            self.__resize(self.size*2)
        # append    
        self.A[self.n] = item
        self.n = self.n + 1

    def pop(self):
        if self.n == 0:
            return 'Empty list'
        print(self.A[self.n-1])
        self.n = self.n-1
        self.size = self.size - 1

    def clear(self):
        self.n = 0
        self.size = 1

    def find(self, value):
        for i in range(self.n):
            if value == self.A[i]:
                return i
        return 'Item not in list'

    def insert(self, position, item):
        if self.n == self.size:
            self.__resize(self.size*2)

        for i in range(self.n, position, -1):
            self.A[i] = self.A[i-1]

        self.A[position] = item
        self.n = self.n + 1

    def __resize(self, new_capacity):
        # create a new array with new capacity
        B = self.__make_array(new_capacity)
        self.size = new_capacity
        # copy the content of A to B
        for i in range(self.n):
            B[i] = self.A[i]
        # reassign A
        self.A = B

    def __make_array(self, capacity):
        # creates a C type array(static, referential) with size capacity
        return (capacity*ctypes.py_object)()

    def remove(self, item):
        res = self.find(item)
        if type(res) == int:
            self.__delitem__(res)
        else: return res

l = DynamicList()
l.append("Hello")
l.append(747)
l.append(True)
l.append(100000)
l.insert(2, "Garry")
print(l)
l.remove(74007)
print(l)


