# ==========================================
#Ejercicio 1 — Verificación de edad

#Un sistema debe determinar si una persona es mayor de edad
# ==========================================

edad = 24

print("Ejercicio 1")

if edad >= 18:
    print("Eres mayor de edad\n")
else:
    print("Eres menor de edad\n")


# ==========================================
#Ejercicio 2 — Acceso

#Un usuario puede acceder a un sistema si:
#- Tiene al menos 18 años
#- Tiene una contraseña correcta
# ==========================================

edad = 22
contraseña_correcta = True

print("Ejercicio 2")

if edad >= 18 and contraseña_correcta == True:
    print("El usuario puede acceder\n")
else:
    print("El usuario NO puede acceder\n")


# ==========================================
#Ejercicio 3 — Métodos de pago

# Una tienda acepta una compra si el cliente:
#Tiene suficiente dinero O Tiene un cupón válido
# ==========================================

dinero = 300
precio = 500
cupon_valido = True

puede_comprar = dinero >= precio

print("Ejercicio 3")

if puede_comprar == True or cupon_valido == True:
    print("El cliente Puede Comprar\n")
else:
    print("El cliente NO puede comprar\n")


# ==========================================
#Ejercicio 4 — Usuario bloqueado

#Un sistema debe determinar si un usuario puede utilizar su cuenta
#La cuenta puede utilizarse cuando NO está bloqueada
# ==========================================

usuario_bloqueado = False
puede_utilizar_cuenta = usuario_bloqueado == True

print("Ejercicio 4")

if usuario_bloqueado == True:
    print("El usuario No puede usar la cuenta\n")
else:
    print("El usuario puede usar la cuenta\n")


# ==========================================
#Ejercicio 5 — Condición compuesta

#Un jugador puede entrar a una zona especial cuando:
#Es mayor de edad Y tiene una entrada válida O Tiene autorización especial
# ==========================================

edad = 18
entrada_valida = True
autorizacion_especial = True

print("Ejercicio 5")

if edad >= 18 and entrada_valida:
    print("El jugado puede ingresar\n")
elif autorizacion_especial == True:
    print("Tienes autorizacion especial\n")
else:
    print("No puedes pasar chamo\n")


# ==========================================
#Ejercicio 6 — Cuenta bancaria

#Un usuario puede retirar dinero si:
#Tiene suficiente saldo Y La cuenta está activa.
# ==========================================

saldo = 800
retiro = 500
cuenta_activa = True

print("Ejercicio 6")

if retiro <= saldo and cuenta_activa:
    print("Generando retiro\n")
elif retiro > saldo and cuenta_activa:
    print("Saldoinsuficiente\n")
elif not cuenta_activa:
    print("Cuenta Inactiva\n")
else:
    print("No hay sistema joven\n")


# ==========================================
#Ejercicio 7 — Acceso a un juego

#Un jugador puede acceder al servidor si:
#Es mayor de edad Y tiene el juego comprado O Es administrador.
# ==========================================

edad = 16
juego_comprado = True
es_administrador = True

edad_valida = edad >= 18
print("Ejercicio 7")

if edad_valida and juego_comprado:
    print("Bienvenido a League Of Legends\n")
elif es_administrador:
    print("soy admin prros :v\n")
else:
    print("Quien sos vos?\n")


# ==========================================
#Ejercicio 8 — Sistema de seguridad

#Una puerta puede abrirse si:
#Se introdujo la contraseña correcta Y la tarjeta es válida O Se utiliza una llave maestra.
# ==========================================

contraseña_correcta = False
tarjeta_valida = True
llave_maestra = True

print("Ejercicio 8")

if contraseña_correcta and tarjeta_valida:
    print("Abriendo puerta\n")
elif llave_maestra:
    print("Acceso de llave Maestra\n")
elif not llave_maestra:
    print("Tus jordan son falsos\n")
else:
    print("Acceso Denegado\n")


# ==========================================
#Ejercicio 9 — Cuenta de usuario

#Un usuario puede utilizar una función especial cuando:
#Tiene una cuenta premium Y la cuenta no está bloqueada O Es administrador.
# ==========================================

cuenta_premium = True
cuenta_bloqueada = False
es_administrador = False

print("Ejercicio 9")

if cuenta_bloqueada == True:
    print("La cuenta esta deshabilitada\n") 
elif es_administrador:
    print("Acceso como administrador\n")
elif cuenta_premium and cuenta_bloqueada == False:
    print("Tienes funciones especiales\n")
else:
    print("Error en el sistema\n")


# ==========================================
#Ejercicio 10 —  Reto

#Un sistema de acceso tiene estas reglas:

#Una persona puede entrar si:

#Primera posibilidad:
#- Tiene 18 años o más
#- Tiene una identificación válida
#- Y no está bloqueada

#Segunda posibilidad:
#- Es administrador

#Tercera posibilidad:
#- Tiene una autorización especial
# ==========================================

edad = 17
identificacion_valida = True
bloqueado = False
es_administrador = False
autorizacion_especial = True

edad_valida = edad >= 18
print("Ejercicio 10")

if (edad_valida and identificacion_valida) and bloqueado == False:
    print("Puedes pasar\n")
elif es_administrador:
    print("Permiso de administrador Aceptado\n")
elif autorizacion_especial:
    print("Permiso de autorizacion especial\n")
elif bloqueado == True:
    print("Cuenta deshabilitada\n")
else:
    print("Kaiju\n")


# ==========================================
#Ejercicio 11 — Sistema de acceso

#Un edificio tiene un sistema de seguridad.

#Una persona puede entrar normalmente cuando:
#- Tiene 18 años o más.
#- Tiene una tarjeta válida.uada
#- La cuenta no está bloqueada.

#Pero existe una regla absoluta:
#- Una cuenta bloqueada nunca puede entrar

#Pero existe una regla absoluta: Una cuenta bloqueada nunca puede entrar.
#Sin embargo, los administradores pueden entrar aunque no tengan tarjeta.
# ==========================================

edad = 21
tarjeta_valida = True
cuenta_bloqueada = False
es_administrador = False

edad_valida = edad >= 18
print("Ejercicio 11")

if cuenta_bloqueada == True:
    print("Cuenta bloqueada\n")
elif edad_valida and tarjeta_valida:
    print("Acceso valido\n")
elif es_administrador:
    print("Acceso beneficio de administrado\n")
else:
    print("Error en el sistema\n")


# ==========================================
#Ejercicio 12 — Compra online

#Una tienda permite realizar una compra bajo estas condiciones:

#El cliente puede comprar si:
#Tiene suficiente dinero Y la cuenta está activa O Tiene un cupón especial.

#Pero: Si la cuenta está bloqueada, la compra debe rechazarse independientemente de las demás condiciones.
# ==========================================

dinero = 800
precio = 600
cuenta_activa = True
cuenta_bloqueada = False
cupon_especial = False

compra_valida = dinero >= precio
print("Ejercicio 12")

if cuenta_bloqueada == True:
    print("Tu cuenta esta bloqueada\n")
elif compra_valida or cupon_especial:
    print("Compra realizada\n")
else:
    print("No puedes realizar la compra\n")


# ==========================================
#Ejercicio 13 — Clasificación de jugador

#Un videojuego tiene diferentes categorías
#Un jugador puede ser considerado Jugador Veterano cuando:

#- Tiene al menos 100 horas de juego
#- Tiene nivel 30 o superior

#Un jugador puede ser considerado Jugador Especial cuando:
#- Tiene una membresía premium

#Pero existe una condición:
#- Un jugador baneado no puede recibir ninguna categoría especial

#Si no cumple ninguna condición, debe clasificarse como:
#- Jugador normal
# ==========================================

horas_jugadas = 150
nivel = 35
membresia_premium = False
jugador_baneado = False

print("Ejercicio 13")

if jugador_baneado:
    print("Cuenta baneada\n")
elif horas_jugadas >= 100 and nivel >= 30:
    print("jugador Veterano\n")
elif membresia_premium:
    print("Jugador premiun\n")
else:
    print("Jugador Normal\n")



# ==========================================
#Ejercicio 14 — Sistema de becas

#Una universidad tiene un sistema de becas.

#Un estudiante puede obtener una beca académica si:
#- Tiene una nota promedio de 4.5 o superior
#- Y tiene al menos 90 % de asistencia

#También puede obtener una beca especial si:
#Tiene una nota promedio de 4.0 o superior Y posee una recomendación especial

#Pero:
#- Un estudiante con una asistencia inferior al 70 % no puede recibir ninguna beca.
# ==========================================

promedio = 4.3
asistencia = 85 
recomendacion_especial = True

print("Ejercicio 14")

if asistencia < 70:
    print("No cumples con el porcentaje de asistencia\n")

elif promedio >= 4.5 and asistencia >= 90:
    print("Cumples con los requisitos de la beca académica\n")

elif promedio >= 4.0 and recomendacion_especial:
    print("Ingresas por recomendación especial\n")
else:
    print("Do you know the way?\n")

#solucion arcaica (tuve complicaciones asi que la simplifique)

print("Ejercicio 14/2")

if asistencia < 70:
    print("No cumples con el porcentaje de asistencia\n")
elif promedio >= 4.5 and asistencia > 90 or promedio >= 4.0 and recomendacion_especial:
    print("Cumples con los requisitos de la beca\n")


# ==========================================
# Ejercicio 15 — Reto final

#Este será el más largo.

#Estás creando un sistema de acceso para una aplicación.
#Un usuario puede acceder si cumple una de estas tres posibilidades:

#Acceso normal

#Debe:
#- Tener 18 años o más.
#- Tener contraseña correcta.
#- Tener la cuenta activa.
#- Acceso premium

#Puede acceder si:
#- Tiene una cuenta premium.
#- La cuenta está activa.
#- Acceso administrativo

#Puede acceder si:
#- Es administrador.

#Pero existen dos reglas especiales:
#- Una cuenta bloqueada nunca puede acceder.
#- Una cuenta suspendida tampoco puede acceder.
# ==========================================

edad = 17
contraseña_correcta = True
cuenta_activa = True
cuenta_premium = False
es_administrador = False
cuenta_bloqueada = False
cuenta_suspendida = False

edad_valida = edad >= 18

print("Ejercicio 15")

if cuenta_suspendida:
    print("Tu cuenta esta suspendida\n")
elif cuenta_bloqueada:
    print("Tu cuenta esta bloqueada\n")
elif es_administrador:
    print("Acceso de administrador\n")
elif edad_valida and contraseña_correcta and not cuenta_suspendida:
    print("Acceso normal\n")
elif cuenta_premium and not cuenta_suspendida:
    print("Acceso premiun\n")
else:
    print("Acceso denegado\n")


# ==========================================
#
# ==========================================