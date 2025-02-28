def karatsuba(x, y):
    if x < 10 or y < 10:
        return x * y
    
    n = max(len(str(x)), len(str(y)))
    m = n // 2
    
    high_x, low_x = divmod(x, 10**m)
    high_y, low_y = divmod(y, 10**m)
    
    P1 = karatsuba(high_x, high_y)
    P2 = karatsuba(low_x, low_y)
    P3 = karatsuba(high_x + low_x, high_y + low_y)
    
    return P1 * 10**(2*m) + (P3 - P1 - P2) * 10**m + P2

if __name__ == "__main__":
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    resultado = karatsuba(num1, num2)
    print(f"O resultado da multiplicação é: {resultado}")
