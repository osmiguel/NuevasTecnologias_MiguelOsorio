def opcion_1():
    print("Elegiste la opción 1")
    # Realizar acciones para la opción 1

def opcion_2():
    print("Elegiste la opción 2")
    # Realizar acciones para la opción 2

def opcion_3():
    print("Elegiste la opción 3")
    # Realizar acciones para la opción 3

def opcion_default():
    print("Opción no válida")

def mostrar_menu():
    print("Menú:")
    print("1. Opción 1")
    print("2. Opción 2")
    print("3. Opción 3")
    opcion = input("Selecciona una opción: ")
    return opcion

opcion = mostrar_menu()

if opcion == "1":
    opcion_1()
elif opcion == "2":
    opcion_2()
elif opcion == "3":
    opcion_3()
else:
    opcion_default()

    
    

    

    