import numpy as np
import matplotlib.pyplot as plt

Delta = 0.01
Umax = -1.0
e0array = np.arange(-1.5 * Umax, Umax + Umax/20, Umax/20)
Uarray = np.array([Umax])  # Solo Umax como en el código original

for U in Uarray:
    NupArray = []
    NdnArray = []
    
    for e0 in e0array:
        
        nup = 0.4
        ndn = 0.6
        nuold = nup
        ndold = ndn
        
        
        for _ in range(101):
            nup = 0.5 - (1.0/np.pi) * np.arctan((e0 + U * ndold)/Delta)
            ndn = 0.5 - (1.0/np.pi) * np.arctan((e0 + U * nuold)/Delta)
            
           
            nuold, ndold = nup, ndn
        
        NupArray.append(nup)
        NdnArray.append(ndn)
    
    
    NupArray = np.array(NupArray)
    NdnArray = np.array(NdnArray)
    Polarization = NupArray - NdnArray  
    
    # Graficar
    plt.figure(figsize=(10, 6))
    plt.plot(e0array, Polarization, 'm-', linewidth=3, label=r'$nup - ndown$')
    plt.axhline(0, color='k', linestyle='--', linewidth=1) 
    
    plt.xlabel(r'$\epsilon_0$', fontsize=22)
    plt.ylabel(r'$nup - ndown$', fontsize=22)
    #plt.title(f'Polarización magnética (U = {U} eV)', fontsize=16)
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    plt.legend(fontsize=16)
    plt.grid(True, alpha=0.3)
    plt.savefig('polar.png')
    plt.show()