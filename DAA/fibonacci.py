def fibonacci_iterative(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b

    return b

n = 10  
result = fibonacci_iterative(n)
print(f"Fibonacci({n}) =", result)

def fibonacci_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Test the recursive Fibonacci function
n = 10 
result = fibonacci_recursive(n)
print(f"Fibonacci({n}) =", result)
