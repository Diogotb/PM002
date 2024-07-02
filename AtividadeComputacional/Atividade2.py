import sympy as sp
import numpy as np

# Definindo a variável
x = sp.symbols('x')

# Definindo a função
f = x * sp.cos(x) * sp.exp(x)

# Calculando as derivadas
f_primeira = sp.diff(f, x)
f_segunda = sp.diff(f_primeira, x)
f_terceira = sp.diff(f_segunda, x)
f_quarta = sp.diff(f_terceira, x)

# Avaliando as derivadas em x = 0
f_0 = f.subs(x, 0)
f_primeira_0 = f_primeira.subs(x, 0)
f_segunda_0 = f_segunda.subs(x, 0)
f_terceira_0 = f_terceira.subs(x, 0)
f_quarta_0 = f_quarta.subs(x, 0)

# Construindo os polinômios de Taylor
T2 = f_0 + f_primeira_0*x + f_segunda_0*x**2/sp.factorial(2)
T3 = T2 + f_terceira_0*x**3/sp.factorial(3)
T4 = T3 + f_quarta_0*x**4/sp.factorial(4)

# Definindo a função para avaliação numérica
f_numeric = sp.lambdify(x, f, 'numpy')
T2_numeric = sp.lambdify(x, T2, 'numpy')
T3_numeric = sp.lambdify(x, T3, 'numpy')
T4_numeric = sp.lambdify(x, T4, 'numpy')

# Ponto de avaliação
x_val = 1 / np.pi**2

# Valores reais e aproximados
f_real = f_numeric(x_val)
T2_approx = T2_numeric(x_val)
T3_approx = T3_numeric(x_val)
T4_approx = T4_numeric(x_val)

# Erros de aproximação
error_T2 = abs(f_real - T2_approx)
error_T3 = abs(f_real - T3_approx)
error_T4 = abs(f_real - T4_approx)

# Resultados
print(f"Valor real de f(x) em x = {x_val}: {f_real:.10f}")
print(f"Valor aproximado por T2(x): {T2_approx:.10f}")
print(f"Erro de aproximação para T2(x): {error_T2:.10f}")
print(f"Valor aproximado por T3(x): {T3_approx:.10f}")
print(f"Erro de aproximação para T3(x): {error_T3:.10f}")
print(f"Valor aproximado por T4(x): {T4_approx:.10f}")
print(f"Erro de aproximação para T4(x): {error_T4:.10f}")
