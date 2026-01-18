def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

temp = float(input("Enter temperature in Celsius: "))
result = celsius_to_fahrenheit(temp)

print("Temperature in Fahrenheit:", result)
