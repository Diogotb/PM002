import matplotlib.pyplot as plt
import numpy as np

# Definindo a função a ser integrada
def f(x):
    return np.cos(x)

# Definindo os limites de integração e o número de subintervalos
a = 0
b = np.pi/2
n = 100

# Calculando a largura de cada subintervalo
dx = (b-a)/n

# Calculando os pontos médios de cada subintervalo
pontos_medios = np.linspace(a+dx/2, b-dx/2, n)

# Calculando a soma de Riemann usando os pontos médios
riemann_soma = np.sum(f(pontos_medios)*dx)


# Valores de x para o gráfico
x_vals = np.linspace(a, b, 1000)
y_vals = f(x_vals)

# Plotando a função
plt.plot(x_vals, y_vals, label='cos(x)')
plt.fill_between(pontos_medios, f(pontos_medios), alpha=0.3, label='Somas de Riemann (Pontos Médios)')
plt.title('Aproximação da Integral usando Somas de Riemann')
plt.xlabel('x')
plt.ylabel('cos(x)')
plt.legend()
plt.show()
