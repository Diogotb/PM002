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

# Imprimindo o resultado
print(f"A aproximação para a integral usando somas de Riemann é: {riemann_soma:.10f}")
