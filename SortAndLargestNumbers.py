#write a program to print the highest 3 values from a dictionary 
d={1:23,2:12,3:55,4:2,5:66,6:3}
print(d)
for i in d:
    print(i)
print(sorted(d.values(),reverse=True)[:3])
