'''
n = int(input("Enter the Size :"))
for i in range (1,n+1):
    space = (2*(n-i))*" " # 2 * 5-1 
    star = ((2*i)-1)*"* "
    print(space+star)
'''

'''
n = int(input("Enter the Size :"))
for i in range (1,n+1):
    space = (2*(n-i))*" "
    star = ((2*i)-1)*"* "
    print(space+star)
for i in range (1,n+1):
    star = (2*(n-i))*"* "
    space = ((2*i)-1)*" "
    print(space+star)
'''

'''
n = int(input("Enter the Size :"))
for i in range (1,n+1):
    space =" " # 2 * 5-1 
    star = ((2*n)-1)*"* "
    print(space+star)
'''

'''
n = int(input("Enter the Size :"))
for i in range (1,n+1):
    star = (n-i) * " *"
    space = i*"  "
    print(space+star)
'''

'''
n = int(input("Enter the Size :"))
for i in range(n):
    if i == 0 or i == n - 1:
        print(" *" * n)  
    else:
        print(" *" + "  " * ((n - 2)*2) + " *") 
'''

'''
l=[1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6, 7, 7]
for num in l:
    if l.count(num)==1:
        print(num)
'''
