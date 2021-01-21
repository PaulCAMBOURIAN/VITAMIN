import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,1,0.0001)

alternative = 2

if alternative == 1:
    steepness = 7 # from 7 to ...
    sig1 = 1/(1+np.exp(-(x-0.5)*steepness))

    plt.plot(x,sig1)
    plt.plot([0.5,0.5],[0,1],'--r')
    plt.plot(x,0.5*np.ones(len(x)),'r')
    plt.plot(x,np.ones(len(x)),'r')
    plt.plot(x,np.zeros(len(x)),'r')
    plt.show()

if alternative == 2:
    
    x = np.arange(0,1,0.0001)
    sig2 = np.log((x+1))/np.log(2)

    plt.plot(x,sig2)
    plt.plot([0.5,0.5],[0,1],'--r')
    plt.plot(x,0.5*np.ones(len(x)),'r')
    plt.plot(x,np.ones(len(x)),'r')
    plt.plot(x,np.zeros(len(x)),'r')
    plt.show()

if alternative == 3:
    
    x = np.arange(0,1,0.0001)
    sig3 = 1/(np.exp((x-0.5)*(-5))+1)-0.075

    plt.plot(x,sig3)
    plt.plot([0.5,0.5],[0,1],'--r')
    plt.plot(x,0.5*np.ones(len(x)),'r')
    plt.plot(x,np.ones(len(x)),'r')
    plt.plot(x,np.zeros(len(x)),'r')
    plt.show()
