#Inverted Star Pyramid / reverse hill pattern

def pattern(n):
    for i in range(n):
        for j in range(i+1):
            print(" ", end='')
        for j in range(i, n-1):
            print("*", end='')
        for j in range(i, n):
            print("*", end='')
        print()
        
n = int(input("Enter the no of rows: "))
pattern(n)

