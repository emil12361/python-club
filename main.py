meme_dict = {
    "CRINGE": "Algo raro o embarazoso",
    "LOL": "Reírse en voz alta",
    "BRB": "Vuelvo enseguida",
    "OMG": "¡Oh Dios mío!",
    "ROFL": "Muerto de risa en el suelo",
    "BTW": "Por cierto",
    "IDK": "No lo sé",
    "TBH": "Para ser honesto",
    "SMH": "Negar con la cabeza / desaprobación",
    "BFF": "Mejores amigos por siempre",
    "YEET": "Lanzar algo con fuerza o entusiasmo",
    "NOOB": "Principiante o novato",
    "SUS": "Sospechoso (de Among Us)",
    "EPIC": "Increíble, muy bueno",
}

# Saludo e instrucciones
print("¡Hola! 😄 Bienvenido al diccionario de palabras graciosas en inglés.")
print("Puedes escribir 5 palabras que no entiendas y te mostraré su significado en español.")
print("Recuerda escribirlas en MAYÚSCULAS como están en el diccionario.\n")

# Bucle para preguntar 5 palabras
for i in range(5):
    word = input("Palabra " + str(i+1) + ": ")
    if word in meme_dict.keys():
        print("Significado: " + meme_dict[word])
    else:
        print("Esa palabra no está en el diccionario 😅")
    print()  # Línea en blanco para separar respuestas
