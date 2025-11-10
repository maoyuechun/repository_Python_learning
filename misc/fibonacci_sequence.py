
def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    seq = [0, 1]
    for i in range(2, n):
        next_value = seq[-1] + seq[-2]
        seq.append(next_value)
    return seq



if __name__ == "__main__":
    n = 20
    print(f"Fibonacci sequence of length {n}: {fibonacci(n)}")