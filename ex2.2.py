__author__ = 'student'
a=['1', '2', '3', '4', '5']
a.insert(0, a[len(a)-1])
print(a[0:len(a)-1])