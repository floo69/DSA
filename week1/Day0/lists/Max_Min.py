n = int(input("Enter n: "))
nums = input("Enter the numbers: ").split()

nums = [int(x) for x in nums]

current_max = nums[0]

for num in nums:
    if num > current_max:
        current_max = num

print(f"Max is {current_max}")
