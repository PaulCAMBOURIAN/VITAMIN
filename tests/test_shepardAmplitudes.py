import numpy as np
import matplotlib.pyplot as plt


f = np.arange(0,1000,1)

#amp = 1 - np.cos(2*np.pi*np.log(f/263)/np.log(2**5))

mu = 200
sigma = 200
amp = np.exp(-((f-mu)/sigma)**2)

plt.plot(f,amp)
plt.xlabel('frequency (Hz)')
plt.show()
