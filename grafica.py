import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np

data = np.loadtxt("datos.dat")

x = np.linspace(1,10,100)
y = np.linspace(-2.84792e+33,4.59037e-41, 100)
plt.plot(x,y)
plt.savefig("resultado.png")
plt.title(4.59037e-41)