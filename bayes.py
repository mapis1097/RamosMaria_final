import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np



pi = 3.1416
N = 100000
aleatorios = [np.random.random()* pi]
sigma = 1.0
variable = 0
a = 1/(sigma*(np.sqrt(2*pi)))

def probabilidad(a,x,sigma):
    return (a*np.exp(-(x)**2/(2*sigma**2)))

for i in range(1,N):
    variable  = aleatorios[i-1] + sigma * ((np.random.random()-0.5))
    distancia = probabilidad(a,variable,sigma)
    variable_2 = np.random.random()
    if(variable_2<distancia):
        aleatorios.append(variable)
    else:
        aleatorios.append(aleatorios[i-1])
        
plt.hist(aleatorios, density=True)
plt.savefig("sigma.png")

plt.show()
