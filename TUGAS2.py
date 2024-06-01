import numpy as np
import matplotlib.pyplot as plt

# Data tegangan (x) dan waktu patah (y)
x = np.array([5, 10, 15, 20, 25, 30, 35, 40])
y = np.array([40, 30, 25, 40, 18, 20, 22, 15])

def lagrange_interpolation(x_points, y_points, x):
    """Menghitung nilai interpolasi menggunakan polinom Lagrange."""
    n = len(x_points)
    result = 0.0
    for i in range(n):
        term = y_points[i]
        for j in range(n):
            if i != j:
                term *= (x - x_points[j]) / (x_points[i] - x_points[j])
        result += term
    return result

# Contoh penggunaan: menghitung nilai interpolasi pada tegangan tertentu
x_targets = [28, 8, 18, 38]  # contoh tegangan yang ingin diinterpolasi
for x_target in x_targets:
    y_interpolated = lagrange_interpolation(x, y, x_target)
    print(f"Waktu patah pada tegangan {x_target} kg/mm² adalah sekitar {y_interpolated:.2f} jam")

# Plot data asli
plt.scatter(x, y, color='green', label='Data asli')

# Plot hasil interpolasi
x_plot = np.linspace(min(x), max(x), 500)
y_plot = [lagrange_interpolation(x, y, xi) for xi in x_plot]
plt.plot(x_plot, y_plot, label='Polinom Interpolasi Lagrange')

plt.xlabel('Tegangan (kg/mm²)')
plt.ylabel('Waktu patah (jam)')
plt.legend()
plt.title('Interpolasi Polinom Lagrange')
plt.show()

# Tambahkan kode testing tambahan
test_points = [5, 10, 15, 20, 25, 30, 35, 40, 8, 18, 28, 38]  # termasuk nilai-nilai dalam data asli dan nilai baru
for tp in test_points:
    interp_value = lagrange_interpolation(x, y, tp)
    print(f"Interpolasi waktu patah pada tegangan {tp} kg/mm² adalah sekitar {interp_value:.2f} jam")
