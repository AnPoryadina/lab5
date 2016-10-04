__author__ = 'student'
a=list(map(int, input().split()))
i=0
while i<len(a):
    if a[i]==2 and a[i+1]==5:
        a.pop(i)
    i=i+1
print(int(sum(a)/len(a)))