# Constant  ----------------------------------------------------------
# Time Complexity O(1)
def toog_constant():
    # data = [1,200,600,500,400,999]
    data = range(1, 1000000000)
    return data[9999]

# print(toog_constant())

#linear ---------------------------------------------------------------
# Time Complexity O(n)
def toog_linerar():
    data = range(1, 11)
    for _ in data:
        print(_)

# toog_linerar()

# logarithmic ------------------------------------------------------------
# this function converst givent integers into string 
# Time Complexity log(n)
def int_to_str(i):
    digits = "0123456789"
    if i == 0:
        return'0'
    result = ''
    while i > 0:
        result = digits[i%10] + result
        i = i // 10 
    return result

# print(int_to_str(10))

# Quadratic --------------------------------------------- 
# Time Complexity O(n)^2

L = [1,2,3,4,5]
M  = [100, 200, 300, 400, 500]
def toog_quadratic():
    for i in L:
        for j in M:
            print(i+j)

# toog_quadratic()

# -----------------------------------------------
# Time Complexity nLog(n)
def toog_exponential():
    n = 1000
    i = k = l = 0

    for i in range(n // 2, n + 1):
        j = 2
        while j <= n:
            k += n // 2
            j *= 2

# Exponential -----------------------------------------------
# Time Complexity < 2^n
def fib(n):
    if n == 1 or n == 0:
        return 1
    else :
        return fib(n-1) + fib(n-1)
    
# print(fib(5))
    


