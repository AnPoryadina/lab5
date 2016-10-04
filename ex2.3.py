__author__ = 'student'
a=[1,5,9,4,7,23,84,7,1,2]
for i in range (0,len(a)-1,1):
    if a.count(a[i])==1:
        print(a[i])