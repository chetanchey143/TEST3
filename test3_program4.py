# 4) Python program to calculate the sum of all the odd numbers within the given range.

a=int(input("enter the number:"))
odd_sum=0
for number in range(1,a+1):
    if number%2!=0:
        odd_sum+=number
        print(odd_sum)