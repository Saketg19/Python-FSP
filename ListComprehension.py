#create a list by taking value from user and print odd numbers
num=[]
for i in range(10):
    i=int(input())
    num.append(i)
even=[num for num in num if num%2==0]
print(even)