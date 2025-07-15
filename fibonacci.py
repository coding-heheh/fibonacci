'''n0 = 0
n1 = 1
n2 = 0
n = int(input('enter the limit: '))
print(n0)
print(n1)
for i in range (n-2):
    n2 = n0+ n1
    print(n2)
    n0 = n1
    n1 = n2'''

def fibonacci(n):
    if n == 0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
num = int(input('enter a limit: '))
# you have to put a loop because its only returning the fibonacci number not the whole list
for i in range (num):
    print(fibonacci(i))

