import numpy as np
import matplotlib.pyplot as plt
import fibseq

N = 10
seq = fibseq.fibonacci(N)

fibonaccimean = np.mean(seq)
fibonaccimedian = np.median(seq)
fibonaccivariance = np.var(seq)

with open("../tex/fibonacci-mean.tex", "w") as f:
     f.write(str(fibonaccimean))

with open("../tex/fibonacci-median.tex", "w") as f:
     f.write(str(fibonaccimedian))

with open("../tex/fibonacci-var.tex", "w") as f:
     f.write(str(fibonaccivariance))