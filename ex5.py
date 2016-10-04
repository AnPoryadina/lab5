__author__ = 'student'
def fib(n,k):
    if n<=k:
        return 1
    else:
        t=0
        for i in range (k,0,-1):
            t=t+fib(n-i,k)
            return t
print(fib(100,0))