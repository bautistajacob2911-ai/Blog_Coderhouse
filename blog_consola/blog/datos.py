perfil_autor = {
    "nombre": "Bautista",
    "Bio": "Aspirante a ingeniero",
    "Especialidad": "Técnico en Informática",
    "Redes_Sociales": ["Instagram:Jacobb_041", "Linkedin: Bautista_Jacob"]
}


estados_post = ("borrador", "publicado", "archivado")
etiquetas_blogs = {"Python", "Arduino", "Electrónica"}


posts = [
    {
        "id": 1,
        "título": "Primeros pasos",
        "estado": estados_post[0],
        "tags": ["Python", "Listas", "variable"],
        "autor": perfil_autor,
        "contenido": "En este post veremos cómo empezar a programar con Python.",
    },
    {
        "id": 2,
        "título": "Arduino",
        "estado": estados_post[1],
        "tags": ["Python", "Diccionarios", "variable"],
        "autor": perfil_autor,
        "contenido": "Django es un framework web creado con Python."
    },
    {
        "id": 3,
        "título": "Electrónica",
        "estado": estados_post[2],
        "tags": ["Python", "Tuplas", "Sets"],
        "autor": perfil_autor,
        "contenido": "Las listas permiten guardar varios elementos en una sola variable."
    },
    {
        "id": 4,
        "título": " ",
        "estado": estados_post[1],
        "tags": ("Python", "Tuplas", "Sets"),
        "autor": perfil_autor,        
        "contenido": "Las listas permiten guardar varios elementos en una sola variable."
    }
]
