#   Codigo que implementa el metodo del trapecio 
#   para aproximar la integral
#   
#
#           Autor:
#   Dr. Ivan de Jesus May-Cen
#   imaycen@hotmail.com
#   Version 1.0 : 11/03/2025
#

import numpy as np
import matplotlib.pyplot as plt

# Definimos la función a integrar
def f(x):
    return x**2+1

# Implementación de la regla del trapecio
def trapezoidal_rule(a, b, n):
    x = np.linspace(a, b, n+1)  # Puntos equidistantes
    y = f(x)
    h = (b - a) / n
    integral = (h / 2) * (y[0] + 2 * sum(y[1:n]) + y[n])  # Regla del trapecio compuesta
    return integral, x, y

# Parámetros de integración
a, b = 0, 2  # Intervalo de integración
n = 4  # Número de subdivisiones

# Cálculo de la integral
integral_approx, x_vals, y_vals = trapezoidal_rule(a, b, n)

# Imprimir el resultado de la integral aproximada
print(f"Integral aproximada con la regla del trapecio: {integral_approx:.6f}")

# Gráfica de la función y la aproximación por trapecios
x_fine = np.linspace(a, b, 100)
y_fine = f(x_fine)

plt.figure(figsize=(8, 5))
plt.plot(x_fine, y_fine, 'r-', label=r'$f(x) = x^2+1$', linewidth=2)
plt.fill_between(x_vals, y_vals, alpha=0.3, color='blue', label="Aproximación Trapecios")
plt.plot(x_vals, y_vals, 'bo-', label="Puntos de integración")

# Etiquetas y leyenda
plt.xlabel("$x$")
plt.ylabel("$f(x)$")
plt.title("Aproximación de la integral con la regla del trapecio")
plt.legend()
plt.grid()

# Guardar la figura
plt.savefig("trapecio.png")
plt.show()

