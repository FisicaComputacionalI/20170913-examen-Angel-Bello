import numpy as np
import matplotlib.pyplot as plt
plt.figure(1)
plt.subplot(211)
x = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]
x1 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]
y = [1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017]
y1 = [1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017]
#ax = plt.subplot(111)
t = np.arange(0.0,21,0.02)
s = np.cos(2*np.pi*t+2014)
t2 = np.arange(0.0, 5.0, 0.02)
line, = plt.plot(t, 10*s+2000, lw=1)
plt.ylim(1996,2017)
plt.plot(x,y,'r--')
plt.plot(x1,y1,'ro')
plt.subplot(212)
plt.plot(t2, np.sin(2*np.pi*t2), 'r--')
plt.savefig('E3.png')
plt.show()
