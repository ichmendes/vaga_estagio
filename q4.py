Python 3.12.5 (tags/v3.12.5:ff3bc82, Aug  6 2024, 20:45:27) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def pertence_fibonacci(n):
...     a, b = 0, 1
...     while b <= n:
...         if b == n:
...             return True
...         a, b = b, a + b
...     return False
... 
... numero = int(input("Informe um número: "))
... if pertence_fibonacci(numero):
...     print(f"{numero} pertence à sequência de Fibonacci.")
... else:
