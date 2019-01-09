import matplotlib.pyplot as plt
import fibseq

N=10

seq = fibseq.fibonacci(N)

fibonacciplot = plt.plot(range(1,N),seq)
plt.savefig("fibonacciplot.pdf")