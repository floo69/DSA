# Pattern-1: Rectangular/sqaure Star Pattern

def pattern(n):
    for i in range(n):
        for j in range(n):
            print("*", end='')
        print()    

n = int(input("Number of rows: "))
pattern(n)
