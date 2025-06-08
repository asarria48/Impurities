import numpy as np
import matplotlib.pyplot as plt


U = 1.0         #repulsion
gamma = 0.1     #width
omega_0 = 0.5   #impurity's energy
omega_F = 1   #Fermi's energy


U_bar = U / gamma
omega_bar = (omega_0 - omega_F) / U


#equation (just for n0_up = n0_down)
def f(n0):
    eq = 1 / np.tan(np.pi * n0 / 2) - 2 * U_bar * (omega_bar + n0 / 2)  
    return eq


n_vals = np.linspace(0.01, 1.99, 300)
f_vals = [f(n) for n in n_vals]


plt.figure(figsize=(8,5))
plt.plot(n_vals, f_vals, label=r'$f(n_0)$')
plt.xlabel(r'$n_0$')
plt.ylabel(r'$f(n_0)$')
plt.title('Auto-consistent solution for $n_0$')
plt.grid(True)
plt.legend()


plt.savefig("autoconsistensol(1).png", dpi=300)
