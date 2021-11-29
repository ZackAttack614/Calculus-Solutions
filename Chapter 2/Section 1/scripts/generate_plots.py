from os import path
import matplotlib.pyplot as plt
import numpy as np

dir = path.abspath(path.join(path.dirname(__file__), '..'))
image_dir = path.join(dir, 'images')

def problem_5(ax):
  height = np.array([-4.9, 15, 0])
  secant = np.array([0.3, 6.125])
  t = np.linspace(0,3,100)

  ax.plot(t, [np.polyval(height, i) for i in t], c='b', label=r'$h(t) = 15t - 4.9t^2$')
  ax.plot(t, [np.polyval(secant, i) for i in t], c='r', linewidth=1, label=r'$h(t) = 0.3t + 6.125$')

  ax.legend()
  ax.grid(True)
  plt.title('Height over time of tossed stone')
  plt.xlabel(r'$t$')
  plt.ylabel(r'$h(t)$')
  plt.savefig(f'{image_dir}/problem_5.png', dpi=500)
  ax.clear()

def problem_8(ax):
  distance = np.array([1, 0, 1, 0])
  secant = np.array([22, -20])
  tangent = np.array([4, -2])
  t = np.linspace(0,5,100)

  ax.plot(t, [np.polyval(distance, i) for i in t], c='b', label=r'$s(t) = t^3 + t$')
  ax.plot(t, [np.polyval(secant, i) for i in t], c='r', linewidth=1, label=r'$s(t) = 22t - 20$')
  ax.plot(t, [np.polyval(tangent, i) for i in t], c='orange', linewidth=1, label=r'$s(t) = 4t - 2$')

  ax.legend()
  ax.grid(True)
  plt.title('Distance traveled of a particle')
  plt.xlabel(r'$t$')
  plt.ylabel(r'$s(t)$')
  plt.savefig(f'{image_dir}/problem_8.png', dpi=500)
  ax.clear()

def problem_9(ax):
  func = np.array([4, 0, -3])
  tangent = np.array([16, -19])
  t = np.linspace(1,3,100)

  ax.plot(t, [np.polyval(func, i) for i in t], c='b', label=r'$P(x) = 4x^2 - 3$')
  ax.plot(t, [np.polyval(tangent, i) for i in t], c='orange', linewidth=1, label=r'$P(x) = 16x - 19$')

  ax.legend()
  ax.grid(True)
  plt.title(r'$f(t)$' + ' with tangent line at ' + r'$t=-9$')
  plt.xlabel(r'$t$')
  plt.ylabel(r'$f(t)$')
  plt.savefig(f'{image_dir}/problem_9.png', dpi=500)
  ax.clear()

def problem_10(ax):
  func = np.array([3, -5])
  tangent = np.array([3, -5])
  t = np.linspace(-10, -8,100)

  ax.plot(t, [np.polyval(func, i) for i in t], c='b', linewidth=2, label=r'$f(t) = 3t - 5$')
  ax.plot(t, [np.polyval(tangent, i) for i in t], c='orange', linewidth=1, label=r'$f(t) = 3t - 5$')

  ax.legend()
  ax.grid(True)
  plt.title(r'$f(t)$' + ' with tangent line at ' + r'$t=-9$')
  plt.xlabel(r'$t$')
  plt.ylabel(r'$f(t)$')
  plt.savefig(f'{image_dir}/problem_10.png', dpi=500)
  ax.clear()

def problem_11(ax):
  def y(x):
    with np.errstate(divide='ignore', invalid='ignore'):
      return 1/(x+2)

  tangent = np.array([-1/16, 3/8])
  x = np.linspace(0, 3, 100)

  ax.plot(x, y(x), c='b', linewidth=2, label=r'$y(x) = \frac{1}{x+2}$')
  ax.plot(x, [np.polyval(tangent, i) for i in x], c='orange', linewidth=1, label=r'$y(x) = \frac{-1}{16}x + \frac{3}{8}$')

  ax.legend()
  ax.grid(True)
  plt.title(r'$y(x)$' + ' with tangent line at ' + r'$x=2$')
  plt.xlabel(r'$x$')
  plt.ylabel(r'$y(x)$')
  plt.savefig(f'{image_dir}/problem_11.png', dpi=500)
  ax.clear()

def problem_12(ax):
  def y(t):
    return np.sqrt(3*t+1)

  tangent = np.array([3/4, 5/4])
  t = np.linspace(0, 3, 100)

  ax.plot(t, y(t), c='b', linewidth=2, label=r'$y(t) = \sqrt{3t+1}$')
  ax.plot(t, [np.polyval(tangent, i) for i in t], c='orange', linewidth=1, label=r'$y(t) = \frac{3}{4}t + \frac{5}{4}$')

  ax.legend()
  ax.grid(True)
  plt.title(r'$y(t)$' + ' with tangent line at ' + r'$t=1$')
  plt.xlabel(r'$t$')
  plt.ylabel(r'$y(t)$')
  plt.savefig(f'{image_dir}/problem_12.png', dpi=500)
  ax.clear()

def problem_13(ax):
  def T(h):
    return 59-0.00356*h

  tangent = np.array([-0.00356, 59])
  h = np.linspace(0, 37_000, 100)

  ax.plot(h, T(h), c='b', linewidth=2, label=r'$T(h) = -0.00356h + 59$')
  ax.plot(h, [np.polyval(tangent, i) for i in h], c='orange', linewidth=1, label=r'$T(h) = -0.00356h + 59$')

  ax.legend()
  ax.grid(True)
  plt.title(r'$T(h)$' + ' with tangent line')
  plt.xlabel(r'$h$')
  plt.ylabel(r'$T(h)$')
  plt.savefig(f'{image_dir}/problem_13.png', dpi=500)
  ax.clear()

if __name__ == '__main__':
  fig, ax = plt.subplots()
  ax.set_facecolor('#EEEEEE')

  problem_5(ax)
  problem_8(ax)
  problem_9(ax)
  problem_10(ax)
  problem_11(ax)
  problem_12(ax)
  problem_13(ax)
