def reverse_number(n):
    rev = 0
    while n > 0:
        x = n % 10
        new_rev = rev * 10 + x
        rev = new_rev
        n = n // 10
    return rev

def is_palindrome(n):
    return n == reverse_number(n)

def even_or_odd(n):
    return "Even" if n % 2 == 0 else "Odd"

def print_table(n):
    for i in range(1, 11):
        print(n, "x", i, "=", n * i)
   
    

num = int(input("Enter a number: "))

print("1. Reverse Number")
print("2. Check Palindrome")
print("3. Check Even/Odd")
print("4. Print Multiplication Table")

choice = int(input("Choose an option: "))

if choice == 1:
    print("Reversed number:", reverse_number(num))
elif choice == 2:
    if is_palindrome(num):
        print("It is a palindrome")
    else:
        print("Not a palindrome")
elif choice == 3:
    print("Number is", even_or_odd(num))
elif choice == 4:
    print(print_table(num))
else:
    print("Invalid choice")
