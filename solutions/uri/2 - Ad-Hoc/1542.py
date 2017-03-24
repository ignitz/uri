# Você começou a competir com seu amigo para ver quem consegue ler mais livros em menos tempo. Seu amigo lia muito mais que você, até o dia que você percebeu que ele lia somente livros muito finos.
# Então você resolveu contar as páginas dos livros, aumentando também a quantidade de páginas lidas por dia. Agora você lê 5 páginas por dia e termina 16 dias antes do que se estivesse lendo 3 páginas por dia. Neste cenário, quantas páginas tem o livro?

# Entrada
# A entrada é composta de vários casos de testes. Cada caso de teste é composto de três números Q (0 < Q < 20), D (0 < D < 20) e P (0 < P < 20) separados por um espaço. Sendo que Q é a quantidade de páginas lidas por dia. D é o número de dias que você adiantaria a leitura caso estivesse lendo a quantidade de páginas informada pelo número P. Um único valor zero indica o fim da entrada.

# Saída
# Para cada caso de teste deverá ser impresso a quantidade de páginas do livro. (Utilize o plural corretamente e não use acentos). Este número deverá ser um inteiro, o qual representa a quantidade de página. Este valor deverá ser truncado caso necessário.

import math

while True:
    args = list(map(int, input().split()))
    if len(args) == 1 and args[0] == 0:
        break
    Q, D, P = args
    # Q*(n+D) = P*n \implies n = DQ/(P-Q)
    n = (D*Q)/(P-Q)
    n = P*n
    n = abs(math.ceil(n))

    if n == 1:
        print(n, 'pagina')
    else:
        print(n, 'paginas')
