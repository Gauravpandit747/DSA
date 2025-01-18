# Linear Search
def linear_search():
    data = [2,4,5,7,8,9,12,14,17,19,22,25,27,28,33,37]
    target = 50
    for i in data:
        if i==target:
            return True
    return False

print(linear_search())