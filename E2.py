import numpy as np
import matplotlib.pyplot as plt
ax = plt.subplot(111)
t = np.arange(0.0,5, 0.01)
s = np.cos(2*np.pi*t+2014)
line, = plt.plot(t, 3*s, lw=1)
plt.ylim(-5,5)
plt.savefig('E2.png')
plt.show()
