#==================================
# Pruebas
#==================================


#================================================
# Ejercicio 1
# Un videojuego cuesta 800 pesos y tiene un descuento del 15 %.
# ¿Cuánto dinero representa el descuento?
#================================================

precio = 800
descuento = 0.15
dinero_descuento = precio * descuento
precio_final = precio - dinero_descuento

print(f"Precio = {precio}")
print(f"Descuento = 15%")
print(f"Dinero descuento = {dinero_descuento}")
print(f"El descuento es de ${dinero_descuento} pesos")
print(f"El precio final del videojuego es ${precio_final} pesos\n")


#================================================
# Ejercicio 2
# Un teclado cuesta 1.200 pesos y tiene un descuento del 25 %.
# ¿Cuál es el precio final del teclado?
#================================================

precio_teclado = 1200
descuento_teclado = 0.25
dinero_descuento_teclado = precio_teclado * descuento_teclado
precio_final_teclado = precio_teclado - dinero_descuento_teclado

print(f"Precio = {precio_teclado}")
print(f"Descuento = 25%")
print(f"Dinero descuento = {dinero_descuento_teclado}")
print(f"El descuento es de ${dinero_descuento_teclado} pesos")
print(f"El precio final del teclado es ${precio_final_teclado} pesos\n")


#================================================
# Ejercicio 3
# Una persona gana 2.000 pesos al mes. Su salario aumenta un 12 %.
# ¿Cuál es su nuevo salario?
#================================================

salario = 2000
aumento = 0.12
nuevo_salario = salario + (salario * aumento)

print(f"Salario = ${salario} pesos")
print(f"Aumento = 12%")
print(f"Nuevo salario = ${nuevo_salario} pesos\n")


#================================================
# Ejercicio 4
# Una computadora cuesta 3.500 pesos.
# Primero aumenta su precio un 10 % y después recibe un descuento
# del 20 % sobre el nuevo precio.
# ¿Cuál es el precio final de la computadora?
#================================================

precio_computadora = 3500
aumento_computadora = 0.10
precio_con_aumento = precio_computadora + (precio_computadora * aumento_computadora)
descuento_computadora = 0.20
precio_final_computadora = precio_con_aumento - (precio_con_aumento * descuento_computadora)

print(f"Precio = ${precio_computadora} pesos")
print(f"Aumento = 10%")
print(f"Precio con aumento = ${precio_con_aumento} pesos")
print(f"Descuento = 20%")
print(f"Precio final = ${precio_final_computadora} pesos\n")


#================================================
# Ejercicio 5
# Una tienda tiene un producto cuyo precio original es de 2.400 pesos.
# La tienda anuncia:
# "Descuento del 30 % y después un descuento adicional del 10 %."
# ¿Cuál es el precio final?
#================================================

producto_precio = 2400
descuento1 = 0.30
precio_con_descuento1 = producto_precio - (producto_precio * descuento1)
descuento2 = 0.10
precio_final = precio_con_descuento1 - (precio_con_descuento1 * descuento2)

print(f"Precio original = ${producto_precio} pesos")
print(f"Descuento 1 = 30%")
print(f"Precio con descuento 1 = ${precio_con_descuento1} pesos")
print(f"Descuento 2 = 10%")
print(f"Precio final = ${precio_final} pesos")