# 7) Python program to find the factorial of a given number.

n=int(input("enter a number: "))
fact=1
for x in range(1,n+1):
    fact*=x
    print("fact of",n,"is:",fact)