def calcular_descuento():
    precio_base = 10

    # Solicitar número de entradas
    entradas = int(input("Ingrese el número de entradas que desea comprar: "))

    # Calcular el total sin descuento
    total_sin_descuento = entradas * precio_base

    # Determinar descuento
    if entradas >= 5:
        descuento = 0.25  
    elif entradas >= 3:
        descuento = 0.15  
    else:
        descuento = 0     

    total_descuento = total_sin_descuento * descuento
    total_a_pagar = total_sin_descuento - total_descuento

    # Resultados
    print("Total sin descuento: $", total_sin_descuento)
    print("Descuento aplicado: $", total_descuento)
    print("Total a pagar: $", total_a_pagar)


def calcular_area_triangulo():
    # Se importa la función sqrt
    from math import sqrt

    # ingresar longitud del lado
    lado = float(input("Ingrese la longitud del lado del triángulo equilátero: "))
    
    # Fórmula para el área de un triángulo equilátero: (sqrt(3)/4) * lado^2
    area = (sqrt(3) / 4) * (lado ** 2)
    
    # Mostrar el resultado
    print("El área del triángulo equilátero es:", area)


def menu_principal():
    while True:
        print("\nMenú Principal")
        print("1. Comprar entradas al cine")
        print("2. Calcular área de un triángulo equilátero")
        print("3. Salir del sistema")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            calcular_descuento()
        elif opcion == "2":
            calcular_area_triangulo()
        elif opcion == "3":
            print("Saliendo del sistema...")
            break  # Salir
        else:
            print("Opción no válida. Intente nuevamente.")

# Ejecución del menú principal
menu_principal()