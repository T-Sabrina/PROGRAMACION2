matrix = []
cont = 1
for fila in range(4):
    matrix.append([])
    for columna in range(4):
        matrix[fila]. append(columna)
        matrix[fila][columna] = cont
        cont = cont + 1

multi = 0
suma = 0

#Diagonal principal
print('Diagonal principal: ')
for d in range(len(matrix)):
    diag = matrix[d][d]
    print(diag)
    suma += diag
    
#Diagonal secundaria
print('Segunda diagonal')
for d in range(len(matrix)):
    diag = matrix[d][-d-1]
    print(diag)
    suma += diag
print(f'suma:{suma}')
