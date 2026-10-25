from blog.datos import posts,estados_post,etiquetas_blogs,perfil_autor
from blog.menu import menu_blog
from blog.operaciones import listar_posts, buscar_por_titulo, filtrar_por_tag
from blog.validaciones import validar_posts


if __name__ == "__main__":
    while True:
        opcion = menu_blog()
        if opcion == 1:
            listar_posts(posts)
        elif opcion == 2:
            termino = input("Ingrese el título del post que desea buscar: ").lower()
            buscar_por_titulo(posts, termino)
        elif opcion == 3:
            tag = input("Ingrese el tag que desea buscar: ").lower()
            filtrar_por_tag(posts, tag)
        elif opcion == 4:
            validar_posts(posts,estados_post)
        elif opcion == 5:
            print("saliendo...")
            break
        else:
            print("Opción inválida, ingrese un número del 1 al 5")



