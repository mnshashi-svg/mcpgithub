# Fibonacci sequence up to 1000

def fibonacci_upto(limit):
    result = []
    a, b = 0, 1
    while a <= limit:
        result.append(a)
        a, b = b, a + b
    return result

if __name__ == "__main__":
    fibs = fibonacci_upto(1000)
    print("Fibonacci sequence up to 1000:")
    print(fibs)
