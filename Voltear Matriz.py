matriz = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

def voltearMatriz(matriz):
    matrizVolteada = [fila[::-1]for fila in matriz]
    return matrizVolteada

matrizVolteada = voltearMatriz(matriz)

print(matrizVolteada)
