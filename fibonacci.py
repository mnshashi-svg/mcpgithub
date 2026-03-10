def fibonacci_till(limit):
    fibs = []
    a, b = 0, 1
    while a <= limit:
        fibs.append(a)
        a, b = b, a + b
    return fibs

if __name__ == "__main__":
    result = fibonacci_till(1000)
    print("Fibonacci numbers till 1000:")
    print(result)
