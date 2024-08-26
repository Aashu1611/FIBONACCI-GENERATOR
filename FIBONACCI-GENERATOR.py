def fibonacci(n):
    fib_sequence = [0, 1]
    
    for i in range(2, n):
        next_value = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_value)
    
    return fib_sequence

n = 10
fib_sequence = fibonacci(n)
print(fib_sequence)
