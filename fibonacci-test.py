import Fibonacci_Sequence as fibonacci


assert len(fibonacci.fibonacci(20)) == 19
assert fibonacci.fibonacci(5) == [1,1,2,3]
a = fibonacci.fibonacci(20)
assert a[18] == a[17] + a[16]

