import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as spi


def f(x):
    return x ** 2


a, b = 0, 2
N = 10000

x_rand = np.random.uniform(a, b, N)
y_rand = np.random.uniform(0, b**2, N)

under_curve = y_rand <= f(x_rand)
monte_carlo_result = (b * b**2) * (np.sum(under_curve) / N)

quad_result, error = spi.quad(f, a, b)

x = np.linspace(-0.5, 2.5, 400)
y = f(x)

fig, ax = plt.subplots()
ax.plot(x, y, 'r', linewidth=2)
ix = np.linspace(a, b)
iy = f(ix)

ax.fill_between(ix, iy, color='gray', alpha=0.3)
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))

plt.grid()
plt.show()

print(f"Значення інтеграла методом Монте-Карло: {monte_carlo_result:.8f}")
print(
    f"Значення інтеграла через фукнцію quad: {quad_result:.8f} (похибка {error})")
