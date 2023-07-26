print("\nWelcome to Our Temperature Converter\n")
print("Enter the value you want to convert : ")
value = float(input())
print("  Enter 1 for Celsius to Fahrenheit converter....")
print("  Enter 2 for Fahrenheit to Celsius converter....")
ans = int(input("\nEnter your value here...   "))
if ans == 1:
    value = (value * +1.8 + 32)
    print(f"\nYour conversion is here.. {value}°F")
elif ans == 2:
    value = ((value - 32) * (5 / 9))
    print(f"\nYour conversion is here.. {(value)}°C")
else:
    print("\nInvalid Input")
