"""
Given a list of integers, calculate the sum and product of all elements.
Example: [1, 2, 3, 4] → Sum: 10, Product: 24
"""
import math

n = int(input("Enter n for sum: "))
mylist = input("Enter numbers for sum: ").split()

for i in range(n):
  mylist[i] = int(mylist[i])

print(f"The sum is {sum(mylist)}")  
  
  
num = int(input("Enter n for product: "))
mylistt = input("enter numbers for prod: ").split()

for i in range(num):
  mylistt[i] = int(mylistt[i])

product = math.prod(mylistt)
print(f"The prod is {product}")