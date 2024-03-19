import numpy as np
import matplotlib.pyplot as plt

def func(x):
    return np.sin(x)

def numerical_integration(func, a, b, n):
    dx = (b - a) / n
    integral = 0
    for i in range(n):
        x = a + i * dx
        integral += func(x) * dx
    return integral

a = 0
b = np.pi
n = 100

integral_value = numerical_integration(func, a, b, n)
print("Numerical Integration Result:", integral_value)

x_values = np.linspace(a, b, 100)
y_values = func(x_values)
plt.plot(x_values, y_values)
plt.fill_between(x_values, y_values, alpha=0.5)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Numerical Integration of sin(x)')
plt.show()
