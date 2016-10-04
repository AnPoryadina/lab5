__author__ = 'student'
a=[1,1,2]
for i in range (0,len(a)-2,1):
    max=a[0]
    n=a.count(a[0])
    if n<a.count(a[i+1]):
        max=a[i+1]
print(max)