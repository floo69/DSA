# Inverted Right Pyramid / Decreasing triangle

def pattern(n):
    for i in range(n):
        for j in range(i, n):
            print("*", end=' ')
        print()

n = int(input("Enter the no of rows: "))
pattern(n)