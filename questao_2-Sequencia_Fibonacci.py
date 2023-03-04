numero = int(input("Informe um número: "))

penultimo = 0
ultimo = 1

while True:
    if numero == ultimo or numero == penultimo:
        resposta = 'O número informado pertence à Sequência de Fibonacci.'
        break
    elif numero < ultimo:
        resposta = 'O número informado NÃO pertence à Sequência de Fibonacci.'
        break
    else:
        penultimo, ultimo = ultimo, ultimo + penultimo
        
print(resposta)
