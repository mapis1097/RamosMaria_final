import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np

data = np.loadtxt("monthrg.dat")

for i in data[:,0]:
    if i > 1900:
        x = np.linspace(1,4632,4632)
        y = data[:,4]
plt.plot(x, data[:,4])
plt.savefig("solar.png")
plt.title("Periodo cada 150 años")
plt.show()

def fourier(x):
    N = len(x)
    X = []
    acumular = 0
    transformada = np.exp(-2*np.pi/N)
    for k in range(N):
        for n in range(N):
            acumular += x[n]*np.exp(-2*1j*np.pi*n*k/N)
        X.append(acumular)
        acumular = 0
    return np.abs(X)