from os import path
import matplotlib.pyplot as plt
import numpy as np

dir = path.abspath(path.join(path.dirname(__file__), '..'))
image_dir = path.join(dir, 'images')

height = np.array([-4.9, 15, 0])
secant = np.array([0.3, 6.125])
t = np.linspace(0,3,100)

fig, ax = plt.subplots()
ax.set_facecolor('#EEEEEE')

# Height of the stone
ax.plot(t, [np.polyval(height, i) for i in t], c='b', label=r'h(t) = 15t - $4.9t^2$')

# Secant line showing average speed
ax.plot(t, [np.polyval(secant, i) for i in t], c='r', label='Secant line of avg. velocity')

ax.legend()
ax.grid(True)
plt.title('Height over time of tossed stone')
plt.xlabel(r'$t$')
plt.ylabel(r'$h(t)$')
plt.savefig(f'{image_dir}/problem_5.png', dpi=500)
