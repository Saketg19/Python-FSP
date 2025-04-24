#fibonacci series
c=int(input("Enter the range : "))
a,b=0,1
print(a,b,end=" ")# here "end" keyword is used to print the values in one line(holds the cursor on th same line)
for i in range(c):
    c=a+b
    print(c,end=" ")
    a,b=b,c