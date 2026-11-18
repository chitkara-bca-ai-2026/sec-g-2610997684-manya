a=float(input("Enter First Number: "))
b=float(input("Enter Second Number: "))

while True:
    print("Select an Operation: ")
    print("1. Addition: ")
    print("2. Subtraction: ")
    print("3. Multiplication: ")
    print("4. Division: ")
    print("5. Modululus/Remainder: ")
    print("6. Power: ")
    print("7. View Calculation History: ")
    print("8. Exit: ")

    choice=input("Enter choice (1-8): ").strip()

    if choice == "1":
        sum=a+b
        print(sum)

    elif choice == "2":
        diff=a-b
        print(diff)

    elif choice == "3":
        mul=a*b
        print(mul)

    elif choice == "4":
        div=a/b
        print(div)

    elif choice == "5":
        mod=a%b
        print(mod)

    elif choice == "6":
        power=a**b
        print(power)

    elif choice == "7":
        print("Calculation History:")
        print(f"Addition: {a} + {b} = {sum}")
        print(f"Subtraction: {a} - {b} = {diff}")
        print(f"Multiplication: {a} * {b} = {mul}")
        print(f"Division: {a} / {b} = {div}")
        print(f"Modulus: {a} % {b} = {mod}")
        print(f"Power: {a} ** {b} = {power}")

    elif choice == "8":
        print("Exiting program.")
        break

    else:
        print("Invalid Input. Please select a valid operation.")