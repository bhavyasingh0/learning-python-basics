a = int(input("Enter a number to reverse: "))
rev = 0
while a>0 :
    x = a % 10 
    new_rev = rev * 10 + x
    rev = new_rev
    a = a // 10
print(rev)