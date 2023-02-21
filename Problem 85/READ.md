Resolução do problema "Counting rectangles" do Project Euler 
(https://projecteuler.net/problem=85)

No caso de um retângulo 1 x 3 seria: 1+2+3=6

Colocando de forma geral:
 
1 x 1 -> 1

1 x 2 -> 1+2

1 x 3 -> 1+2+3

1 x 4 -> 1+2+3+4

1 x 5 -> 1+2+3+4+5

De acordo com https://pt.wikipedia.org/wiki/1_%2B_2_%2B_3_%2B_4_%2B_%E2%8B%AF, a soma de todos os números naturais até n (1 + 2 + 3 + 4 + · · · + n) é dada por n(n+1)/2.

Adicionando as mais m linhas, multilplicamos as possibilidades das somas de n e m, dando a seguinte fómula: (n(n+1)/2) * (m(m+1)/2).

Encontrada a fómula para calcular o número de retângulos, devemos encontrar o m e n mais próximos de uma grade retangular de dois milhões de retângulos.

Para colocar um limite nas interações, considerando n=2, procuramos o valor de m : 

(2(2+1)/2) * (m(m+1)/2) = 2000000 ->
(m(m+1)/2) = 666666.66 -> 
m^2 + m = 1333333.33 -> x = apx. 1154

Então, foi feito em Python, um código que busca a menor diferença de 2000000 para valores m e n diferentes. Calculando a área (mxn) ao mesmo tempo, que é o resultado da questão.


