def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib = [0, 1]
        for i in range(2, n):
            fib.append(fib[i-1] + fib[i-2])
        return fib

numero = int(input("Informe um número: "))
fibonacci_list = fibonacci(numero)

if numero in fibonacci_list:
    print(f"O número {numero} pertence à sequência de Fibonacci: {fibonacci_list}")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci: {fibonacci_list}")
