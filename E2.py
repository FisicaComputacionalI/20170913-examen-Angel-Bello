import numpy as np
import matplotlib.pyplot as plt
ax = plt.subplot(111)
t = np.arange(0.0,5, 0.01)
#La magnitud de la funci'on coseno multiplica al coseno. Si entraste en el 2014, al menos llevas 3 anios. La constante se suma a la funci'on no al argumento. 
#La definici'on m'as apropiada ser'ia 3*np.cos(2*np.pi*t)+2014
s = np.cos(2*np.pi*t+2014)
line, = plt.plot(t, 3*s, lw=1)
plt.ylim(-5,5)
plt.savefig('E2.png')
plt.show()
