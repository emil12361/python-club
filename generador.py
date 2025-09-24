import random  # Importamos la librería para elegir caracteres aleatorios

# 1️⃣ Todos los caracteres posibles para la contraseña
caracteres = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

# 2️⃣ Pedimos al usuario la longitud de la contraseña
longitud = int(input("¿Cuántos caracteres quieres que tenga tu contraseña? "))

# 3️⃣ Creamos la variable donde guardaremos la contraseña
contraseña = ""

# 4️⃣ Usamos un bucle para seleccionar caracteres aleatorios y agregarlos a la contraseña
for i in range(longitud):
    contraseña = contraseña + random.choice(caracteres)

# 5️⃣ Mostramos la contraseña resultante
print("Tu contraseña generada es:")
print(contraseña)
