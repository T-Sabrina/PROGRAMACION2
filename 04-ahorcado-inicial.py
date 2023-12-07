import random		
IMÁGENES_AHORCADO = ['''		
  +---+		
  |   |		
      |		
      |		
      |		
      |		
  =========''', '''		
  +---+		
  |   |		
  O   |		
      |		
      |		
      |		
  =========''', '''		
  +---+		
  |   |		
  O   |		
  |   |		
      |		
      |		
  =========''', '''		
  +---+		
  |   |		
  O   |		
 /|   |		
      |		
      |		
  =========''', '''		
  +---+		
  |   |		
  O   |		
 /|\  |		
      |		
      |		
  =========''', '''		
  +---+		
  |   |		
  O   |		
 /|\  |		
 /    |		
      |		
  =========''', '''		
  +---+		
  |   |		
  O   |		
 /|\  |		
 / \  |		
      |		
  =========''']		
palabras = 'hormiga babuino tejon murcielago oso castor camello gato almeja cobra pantera coyote cuervo ciervo perro burro pato aguila huron zorro rana cabra ganso halcon leon lagarto llama topo mono alce raton mula salamandra nutria buho panda loro paloma piton conejo carnero rata cuervo rinoceronte salmon foca tiburon oveja mofeta perezoso serpiente araña cigüeña cisne tigre sapo trucha pavo tortuga comadreja ballena lobo cebra'.split()
def buscarPalabraAleat(listaPalabras):
    palabraAleatoria = random.randint(0, len(listaPalabras) - 1)
    return listaPalabras[palabraAleatoria]

def displayBoard(IMÁGENES_AHORCADO, letraIncorrecta, letraCorrecta, palabraSecreta):
    print(IMÁGENES_AHORCADO[len(letraIncorrecta)])
    print ("")
    fin = " "
    print ('Letras incorrectas:', fin)
    for letra in letraIncorrecta:
        print (letra, fin)
    print ("")
    espacio = '_' * len(palabraSecreta)
    for i in range(len(palabraSecreta)):
        if palabraSecreta[i] in letraCorrecta:
            espacio = espacio[:i] + palabraSecreta[i] + espacio[i+1:]
    for letra in espacio:
        print (letra, fin)
    print ("")

def elijeLetra(algunaLetra):
    while True:
        print ('Adivina una letra:')
        letra = input()
        letra = letra.lower()
        if len(letra) != 1:
            print ('Introduce una letra')
        elif letra in algunaLetra:
            print ('Ya nombraste esa letra ¿Qué tal si pruebas con una diferente?')
        elif letra not in 'abcdefghijklmnopqrstuvwxyz':
            print ('Ingresa una letra.')
        else:
            return letra
        
def empezar():
    print ('¿Quieres jugar de nuevo? (Si o NO)')
    return input().lower().startswith('s')

print('A H O R C A D O')
letraIncorrecta = ""
letraCorrecta = ""
palabraSecreta = buscarPalabraAleat(palabras)
finJuego = False
while True:
    displayBoard(IMÁGENES_AHORCADO, letraIncorrecta, letraCorrecta, palabraSecreta)
    letra = elijeLetra(letraIncorrecta + letraCorrecta)
    if letra in palabraSecreta:
        letraCorrecta = letraCOrrecta + letra
        letrasEncontradas = True
        for i in range(len(palabraSecreta)):
            letrasEncontradas = False
            break
        if letrasEncontradas:
            print ('¡Muy bien! La palabra secreta es "' + palabraSecreta + '"! ¡Has ganado!')
            finJuego = True
    else:
        letraIncorrecta = letraIncorrecta + letra
        if len(letraIncorrecta) == len(AHORCADO) - 1:
            displayBoard(IMÁGENES_AHORCADO, letraIncorrecta, letraCorrecta, palabraSecreta)
            print ('¡Se ha quedado sin letras!\nDespues de ' + str(len(letraIncorrecta)) + ' letras erroneas y ' + str(len(letraCorrecta)) + ' letras correctas, la palabra era "' + palabraSecreta + '"')
            finJuego = True
    if finJuego:
        if empezar():
            letraIncorrecta = ""
            letraCorrecta = ""
            finJuego = False
            palabraSecreta = buscarPalabraAleat(palabras)
        else:
            break
