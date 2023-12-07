#Sorteo de estudiantes 2.0
import random
listaOrdenada = []
nombres = ['sabri', 'cele', 'yane', 'sofi']
for i in range(len(nombres)):
    x = random.randint(0,len(nombres)-1)
    listaOrdenada.append(nombres[x])
    del (nombres[x])
print(listaOrdenada)
