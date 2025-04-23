#Largest 3 numbers
lst=[]
for i in range(10):
    i=int(input())
    lst.append(i)
lst.sort(reverse=True)
print(lst[:3])
    