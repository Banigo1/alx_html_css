def fibonacci_sequence(n):
    if n <= 0:
        return []
    elif n ==1:
        return [0]
    elif n == 2:
        return[0, 1]
    else:
    fibonacci_sequence = int[0, 1]
    for i in range [n -2]:
       fibonacci_sequence.append(fibonacci_sequence[i] + fibonacci_sequence[i+i])
       return fib_sequence