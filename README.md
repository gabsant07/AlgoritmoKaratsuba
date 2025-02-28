# Projeto AlgoritmoKaratsuba

## Descrição do Projeto
Este projeto tem como objetivo a implementação do Algoritmo de Karatsuba em Python, um método eficiente para multiplicação de números inteiros grandes. O algoritmo tem o objetivo de reduzir a complexidade computacional da multiplicação em comparação ao método tradicional.

## Como executar o projeto

### Requisitos
- Python instalado

### Nota técnica

1 etapa.
Clonar o repositório:
bash
   git clone https://github.com/gabsant07/AlgoritmoKaratsuba.git

2 etapa.
Acessar o diretório do projeto:
 bash
   cd AlgoritmoKaratsuba-python

3 etapa.
Executar o main:
 bash
   python karatsuba.py

4 etapa.
Digitar dois números para realizar uma multiplicação e mostrar o resultado.

## Implementação do Algoritmo de Karatsuba

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

## Análise da Complexidade do Algoritmo

### Complexidade Assintótica
- Melhor Caso: O(n^log2^(3)) ≈ O(n^1.58)
- Caso Médio: O(n^log2^(3)) ≈ O(n^1.58)
- Pior Caso: O(n^log2^(3)) ≈ O(n^1.58)

### Complexidade Ciclomática

Número de arestas (E): 8
Número de nós (N): 7
Número de componentes conexos (P): 1
Complexidade Ciclomática (M) = E - N + 2P = 8 - 7 + 2(1) = 3
