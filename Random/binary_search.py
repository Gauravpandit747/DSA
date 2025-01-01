data = [2,4,5,7,8,9,12,14,17,19,22,25,27,28,33,37]
# data = range(1,1000000000)

# Binary Iterative Search 
def binary_search_iterative(data, target):
    low = 0 
    high = len(data) - 1

    while high >= low:
        mid = (low+high) // 2
        if target == data[mid]:
            return True
        elif target< data[mid]:
            high = mid-1
        else:
            low = mid+1
    return False

# print(binary_search_iterative(data, 100))
# Binary Recursive search
def binary_search_recursive(data, target, low, high):
    if low > high:
        return False
    else:
        mid = (low + high) // 2 
        if target == data[mid]:
            return True
        elif target < data[mid]:
            high = mid - 1
            return binary_search_recursive(data, target, low, high)
        else:
            low = mid + 1
            return binary_search_recursive(data, target, low, high)

# print(binary_search_recursive(data, 2, 0, len(data) - 1))
