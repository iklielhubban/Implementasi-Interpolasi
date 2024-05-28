import numpy as np
import matplotlib.pyplot as plt
from lagrange_interpolation import lagrange_interpolation
from newton_interpolation import newton_interpolation

# Data yang diberikan
x_data = np.array([5, 10, 15, 20, 25, 30, 35, 40])
y_data = np.array([40, 30, 25, 40, 18, 20, 22, 15])

# Rentang x untuk plotting
x_plot = np.linspace(5, 40, 400)

# Interpolasi menggunakan kedua metode
y_lagrange = lagrange_interpolation(x_plot, x_data, y_data)
y_newton = newton_interpolation(x_plot, x_data, y_data)

# Plotting hasil interpolasi
plt.figure(figsize=(12, 6))
plt.plot(x_data, y_data, 'o', label='Data', markersize=10)
plt.plot(x_plot, y_lagrange, label='Lagrange Interpolation', linestyle='--')
plt.plot(x_plot, y_newton, label='Newton Interpolation', linestyle='-.')
plt.xlabel('Tegangan (kg/mm^2)')
plt.ylabel('Waktu Patah (jam)')
plt.title('Interpolasi Polinom Lagrange dan Newton')
plt.legend()
plt.grid(True)
plt.show()