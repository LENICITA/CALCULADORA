import math

opcion = 0

while opcion != 4:
    print("Menú")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")

    opcion = input("Selecciona una opción (1-5): ")

    if opcion == "1":
        print("Has escogido la operación: Suma")
    elif opcion == "2":
        opcion1 = int (input ("Digite el primer Numero: "))
        opcion2 = int (input ("Digite el segudo Numero: "))

        resultado  = (opcion1 - opcion2)

        print ("el resultado de la resta es: ",resultado)   
    
    elif opcion == "3":
        print("Has escogido la operación: Multiplicacion")
    elif opcion == "4":
        print("Has escogido la operación: Division")
    
    else:
        print("Opción no válida. Intenta de nuevo.")

