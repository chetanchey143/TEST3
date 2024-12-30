# 5) Python program to calculate the sum of all the even numbers within the given range.

a1=int(input("enter the number: "))
sum=0
for x in range(1,a1+1):
    if x%2==0:
        sum+=x
        print(sum)
