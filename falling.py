import numpy as np
import math as mt


r = np.array([0, 0, 100])
v = np.array([0, 0, 0])
Nt = 10000
dt = 0.01
g = np.array([0, 0, -9.81])
t = 0
for i in range(0, Nt):
    r = r + dt*v
    v = v + dt*g
    t = t + dt
    if r[2] <= 0:
        print(t)
        break
print(r)
