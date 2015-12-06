import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(1)
x = np.arange(10.0)/10.0
y = (x + 0.1)**2

plt.errorbar(x, y, xerr=0.1)
y = (x + 0.1)**3

plt.errorbar(x + 0.6, y, xerr=0.1)

y = (x + 0.1)**4
plt.errorbar(x + 1.2, y, xerr=0.1)

plt.xlim(-0.2, 2.4)
plt.ylim(-0.1, 1.3)


plt.show()