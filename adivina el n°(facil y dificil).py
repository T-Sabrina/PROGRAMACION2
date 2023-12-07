import random
intrealizados=0
dificil=2
facil=1
print('Elija una dificultad')
print('facil=1 o dificil=2')
r=int(input('-->'))
if(r==1 or r==2):
    
    if(r==1):
        sec = random.randint(1,20)
        while(intrealizados<=6):
            print('ingrese un número')
            x=int(input('-->'))
            intrealizados=intrealizados+1
            if(x<sec):
                print('el numero ingresado es menor que el secreto')
                
            else:
                if(x>sec):
                    print('el numero ingresado es mayor que el secreto')
                    
                else:
                    if(x==sec):
                        break
        print('¡Felicidades!, has adivinado')
    else:
        sec=random.randint(1,200)
        while(intrealizados<=7):
            print('ingrese un numero')
            x=int(input('-->'))
            intrealizados=intrealizados+1
            if(x<sec):
                print('el numero ingresado es menor que el secreto')
                
            else:
                if(x>sec):
                    print('el numero ingresado es mayor que el secreto')
                    
                else:
                    if(x==sec):
                        break
        print('¡Felicidades!, has adivinado')
                    
else:
    print('Opcion invalida')
