# conversor v 0.1
# By: miguel gomez lopez
from pip.backwardcompat import raw_input


def conversor1():
    while True:
        try:
            print("a cuanto esta el precio del dolar en mexico ----")
            global b
            b=input()
            b=float(b)
        except ValueError:
            print ("por favor digita una cantidad no una letra")
        else:
            print("Cuantos dolares tienes")
            global dolares
            dolares=input()
            dolares=float(dolares)
            c=(b*dolares)
            print("Usted tiene=",c,"pesos en dolares")
            print()
            break
def conversor2():
    print("a cuanto esta el precio del dolar en mexico")
    global b
    b=input()
    b=float(b)

    print("Cuantos pesos tienes")
    global dolares
    dolares=input()
    dolares=float(dolares)

    c=(dolares/b)
    print("Usted tiene=",c,"dolares")

def conversor3():
    print("a cuanto esta el precio del dolar en mexico")
    global b
    b=input()
    b=float(b)

    print("a cuanto esta el precio del euro en mexico")
    global a
    a=input()
    a=float(a)

    print("Cuantos dolares tienes")
    global dolares
    dolares=input()
    dolares=float(dolares)
    c=(b/a)
    d=(c*dolares)
    print("Usted tiene=",d,"euros ")

def conversor4():
    print("a cuanto esta el precio del dolar en mexico")
    global b
    b=input()
    b=float(b)

    print("a cuanto esta el precio del Yen en mexico")
    global a
    a=input()
    a=float(a)

    print("Cuantos dolares tienes")
    global dolares
    dolares=input()
    dolares=float(dolares)

    c=(b/a)
    d=(c*dolares)
    print("Usted tiene=",d,"Yenes ")


def menu ():
    print("                    W.E.L.C.O.M.E")
    print ("Bienbenido al programa de conversion de efectivo")
    print()
    print (        "Menu :")
    print ("1. ) Convercion de pesos a dolares")
    print ("2. ) Convercion de dolares a pesos")
    print ("3. ) Convercion de dolares a euros")
    print ("4. ) Convercion de dolares a yenes")
    print ("5. ) Salir ")
    print()
    print()
menu()
while True:

    try:
        opcion=int(raw_input("Que opcion deseas realizar de la lista  -->"))
        print()
    except ValueError:
         print ("¡Huy! No es un número. Prueba de nuevo...")
    else:

        if opcion == 1:
             print("Usted eligio convertir Pesos a Dolares")
             print()
             print(conversor1())
             print("Escribe 5 para salir o Escribe 6 para volver aver el menu")

        elif opcion == 2:
             print("Usted eligio convertir Dolares a pesos")
             print()
             print (conversor2())
             print("Escribe 5 para salir o Escribe 6 para volver aver el menu")
        elif opcion == 3:
             print("Usted eligio convertir Dolares a Euros")
             print()
             print (conversor3())
             print("Escribe 5 para salir o Escribe 6 para volver aver el menu")

        elif opcion == 4:
             print("Usted eligio convertir Dolares a Yenes")
             print()
             print (conversor4())
             print("Escribe 5 para salir o Escribe 6 para volver aver el menu")
        elif opcion >=7:
              print("Usuario estas equivocado digita un numero del 1 al 5")
              print()
              print(menu())
        elif opcion ==5:
              print("")
              print(" Usted acaba de salir gracias por utilizarme")
              break
        elif opcion ==6:
              print(menu())





