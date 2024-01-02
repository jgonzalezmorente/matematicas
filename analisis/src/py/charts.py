import numpy as np
import matplotlib.pyplot as plt

# Definir el rango de valores para x y y
x = np.linspace(-2, 2, 100)
y = np.linspace(-2, 2, 100)

# Crear una malla de coordenadas a partir de x y y
X, Y = np.meshgrid(x, y)

# Calcular los valores de Z para la función dada
Z = (X**2 + 3*Y**2) * np.exp(1 - X**2 - Y**2)

# Crear una figura para los gráficos
fig = plt.figure(figsize=(12, 6))

# Agregar un subplot para la gráfica 3D
ax1 = fig.add_subplot(1, 2, 1, projection='3d')
ax1.plot_surface(X, Y, Z, cmap='viridis') # type: ignore
#ax1.set_title('Gráfica 3D de z=(x^2 + 3y^2)e^{1-x^2-y^2}')
ax1.set_xlabel('$x$')
ax1.set_ylabel('$y$')
ax1.set_zlabel('$z$') # type: ignore

# Agregar un subplot para las curvas de nivel
ax2 = fig.add_subplot(1, 2, 2)
contour = ax2.contour(X, Y, Z, 20, cmap='viridis') # 20 curvas de nivel, 'viridis' es un mapa de colores
fig.colorbar(contour, ax=ax2)
#ax2.set_title('Curvas de nivel de z=(x^2 + 3y^2)e^{1-x^2-y^2}')
ax2.set_xlabel('$x$')
ax2.set_ylabel('$y$')

# Ajustar el espacio entre subtramas
plt.subplots_adjust(wspace=0.4)

# Mostrar la gráfica
plt.show()
