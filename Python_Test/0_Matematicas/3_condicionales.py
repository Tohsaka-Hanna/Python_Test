#==================================
# Tema 2: Condicionales
#==================================


#================================================
# Ejercicio 1 — Precio
# Una tienda tiene un producto que cuesta 1.500 pesos.

# - Si el precio es mayor a 1.000, muestra "Producto caro".
# - Si no, muestra "Producto económico".

# Tu programa debe decidir qué mensaje mostrar.
#================================================

precio_producto = 1500

if precio_producto > 1000:
    print("Producto caro\n")
else:
    print("Producto económico\n")


#================================================
# Ejercicio 2 — Edad
# Una persona tiene una edad determinada.

# - Menor de 13 → "Niño"
# - De 13 a 17 → "Adolescente"
# - 18 o más → "Adulto"

# Haz que Python determine automáticamente la categoría.
#================================================

edad = 20

if edad < 13:
    print("Niño\n")
elif edad <= 17:
    print("Adolescente\n")
else:
    print("Adulto\n")


#================================================
# Ejercicio 3 — Temperatura
# Una habitación tiene una temperatura de 27 °C.

# - Menos de 18 → "Frío"
# - Entre 18 y 25 → "Templado"
# - Más de 25 → "Caliente"

# Haz que Python determine el estado.
#================================================

temperatura = 27

if temperatura < 18:
    print("Frío\n")
elif temperatura <= 25:
    print("Templado\n")
else:
    print("Caliente\n")


#================================================
# Ejercicio 4 — Matemático
# Un número puede ser:

# - Positivo.
# - Negativo.
# - Cero.

# Crea un programa que reciba un número y determine
# cuál de las tres posibilidades es.
#================================================

numero = -5

if numero > 0:
    print("Positivo\n")
elif numero < 0:
    print("Negativo\n")
else:
    print("Cero\n")


#================================================
# Ejercicio 5 — Razonamiento
# Una tienda tiene esta regla:

# - Compra menor de 500 → sin descuento.
# - Compra entre 500 y 999 → 10 % de descuento.
# - Compra de 1.000 o más → 20 % de descuento.

# El cliente realiza una compra de 1.250 pesos.
# Tu programa debe:
# - Determinar qué descuento corresponde.
# - Calcular cuánto dinero representa el descuento.
# - Calcular el precio final.
# - Mostrar toda la información.
#================================================

descuento = 0
compra = 1000
descuento_menor = 0.10
descuento_mayor = 0.20

if compra < 500:
    descuento = compra * 0

elif compra < 1000:
    descuento = compra * descuento_menor

else:
    descuento = compra * descuento_mayor

print(f"Compra = ${compra} pesos")
print(f"Descuento = ${descuento} pesos")
print(f"Precio final = ${compra - descuento} pesos")


#==================================
#
#==================================