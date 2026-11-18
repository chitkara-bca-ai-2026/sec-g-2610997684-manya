
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

while True:
    print("MATHEMATICS LEARNING TOOL")
    print("Select an operation:")
    print("1. Calculate Factorial")
    print("2. Generate Fibonacci Series")
    print("3. Exit")

    ch = input("Enter choice (1-3): ")

    if ch == "1":
        val = int(input("Enter a non-negative integer: "))
        if val >= 0:
            result = factorial(val)
            print(f"[RESULT] Factorial of {val} ({val}!) = {result}")

    elif ch == "2":
        num_terms = int(input("Enter number of terms to generate: "))
        if num_terms >= 0:
            fib_list = []
            for i in range(num_terms):
                fib_list.append(fibonacci(i))
            print(f"[RESULT] Fibonacci series ({num_terms} terms): {fib_list}")

    elif ch == "3":
        print("Thank you for using the Mathematics Learning Tool. Goodbye!")
        break

    else:
        print("Invalid choice, try again.")
