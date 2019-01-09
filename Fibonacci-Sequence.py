def fibonacci(n):
    """Returns the n th fibonacci number"""
    if n in [0, 1]:  # The special case of n being 0 or 1
        return 1
    a = 1  # Setting the starting values
    b = 0
    fib_sequence=[]
    for i in range(n - 1):  # Going through the first n - 1 terms
        temp = b  # A temporary variable to remember the value of b
        b = a + b  # New value of b
        fib_sequence.append(b)
        a = temp  # New value of a (old value of b)
    return fib_sequence
