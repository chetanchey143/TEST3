# 3)Python program to calculate the sum of all numbers from 1 to a given number.

n = int(input("Enter a number: "))
total_sum = 0
for number in range(1, n + 1):
    total_sum += number
print("The sum of all numbers from 1 to",n,"is:",total_sum)





