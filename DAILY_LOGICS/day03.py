
'''
L=[1, 2, 3, 4, 6, 7, 8]
end = L[-1]
for i in range (1, end + 1):
    present = False
    for j in L:
        if i==j:
            present = True
            break 
    if not(present):
        print(i)
'''


'''
value = input()
rev = value[::-1]
if value == rev :
    print("Its a Palindrome")
else:
    print("Its not a Palindrome")
'''