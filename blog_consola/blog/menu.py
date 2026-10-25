def menu_blog():
    print("\n---MENÚ DEL BLOG---")
    print("1. Ver todos los posts")
    print("2. Buscar por título")
    print("3. Filtrar por tag")
    print("4. Validar posts")
    print("5. Salir")
    try:
        opcion = int(input("Seleccione una opción: "))
        return opcion
    except ValueError:
        print("Opción inválida, ingrese un número del 1 al 5")