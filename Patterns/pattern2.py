#Right-Angled Triangle Pattern / increasing triangle

def pattern(n):
    for i in range(n):
        for j in range(i+1):
            print("*" , end=' ')
        print()

n = int(input("Enter the no of rows: "))
pattern(n)