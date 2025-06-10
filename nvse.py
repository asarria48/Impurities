import numpy as np
import matplotlib.pyplot as plt

Delta = 0.2
Umax = -1
e0array = np.arange(-1.5*Umax, Umax + Umax/20, Umax/20)
Uarray = np.array([Umax])  

for U in Uarray:
    NupArray = []
    NdnArray = []
    
    for e0 in e0array:
        nup = 0.6
        ndn = 0.4
        nuold = nup
        ndold = ndn
        num1 = nup
        ndm1 = ndn
        
        for ii in range(101):  
            nup = 0.5 - (1.0/np.pi) * np.arctan((e0 + U*ndold)/Delta)
            ndn = 0.5 - (1.0/np.pi) * np.arctan((e0 + U*nuold)/Delta)
            
            num1 = nuold
            ndm1 = ndold
            nuold = nup
            ndold = ndn
        
        NupArray.append(nup)
        NdnArray.append(ndn)
    
   
    NupArray = np.array(NupArray)
    NdnArray = np.array(NdnArray)
    
   
    plt.figure(figsize=(10, 6))
    plt.plot(e0array, NupArray + NdnArray, 'k-', linewidth=3, label='<Nup>+<Ndown>')
    plt.plot(e0array, NdnArray, 'r-x', label='<Ndown>')
    plt.plot(e0array, NupArray, 'b-o', label='<Nup>')
    
    plt.xlabel('ε₀', fontsize=22)
    plt.ylabel('<n>', fontsize=32)
    plt.xticks(fontsize=22)
    plt.yticks(fontsize=22)
    plt.legend(fontsize=16)
    plt.grid(True)
    plt.savefig('ocupvse0.png')
    plt.show()