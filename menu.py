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
        n1 = float(input("Digite el primer Numero: "))
        n2 = float(input("Digite el segundo Numero: "))

        resultado  = (n1 + n2)

        print ("el resultado de la suma es: ",resultado)

    elif opcion == "2":
        print("Has escogido la operación: Resta")
    elif opcion == "3":
        print("Has escogido la operación: Multiplicacion")
    elif opcion == "4":
        print("Has escogido la operación: Division")
    else:
        print("Opción no válida. Intenta de nuevo.")

