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
        print("Has escogido la operación: Resta")
    elif opcion == "3":
        print("Has escogido la operación: Multiplicacion")
    elif opcion == "4":
        print("Has escogido la operación: Division")
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
    
        resultado = num1 / num2
        print("El resultado de la división es: ", resultado)
    
    else:
        print("Opción no válida. Intenta de nuevo.")

