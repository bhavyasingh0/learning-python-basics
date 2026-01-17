a = int(input("Enter a number to check if palindrome: "))
org = a
rev = 0
while a>0 :
    l = a % 10 
    new_rev = rev * 10 + l
    rev = new_rev
    a = a // 10
if org == rev:
        print("It's a Palindrome number!")
else:
        print("Not palindrome number :(")