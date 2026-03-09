def fibonacci_upto(limit):
    sequence = []
    a, b = 0, 1
    while a <= limit:
        sequence.append(a)
        a, b = b, a + b
    return sequence

fib_numbers = fibonacci_upto(3000)
print(f"Fibonacci numbers up to 3000:")
print(fib_numbers)
