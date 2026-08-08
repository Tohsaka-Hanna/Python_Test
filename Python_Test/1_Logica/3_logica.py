# ==========================================
# Ejercicio 3 — Cajero automático
#
# Un cajero automático debe permitir realizar un retiro.
#
# El usuario proporciona:
# - Saldo disponible en su cuenta.
# - Cantidad de dinero que desea retirar.
# - Si la cuenta está activa.
#
# El retiro solamente puede realizarse cuando:
# - La cuenta está activa.
# - El monto a retirar es mayor que 0.
# - El usuario tiene suficiente saldo.
#
# Si el retiro es válido:
# - Calcular el nuevo saldo.
# - Mostrar el monto retirado.
# - Mostrar el saldo restante.
#
# Si el retiro no puede realizarse, el programa debe
# determinar cuál es el motivo:
#
# - Cuenta inactiva.
# - Monto inválido.
# - Saldo insuficiente.
#
# Finalmente, muestra un pequeño resumen de la operación
# utilizando f-strings.
# ==========================================


usuario = "Hanna"
saldo_actual = 800
retiro = 500

saldo_restante = saldo_actual - retiro

cuenta_bloqueada = False

print(f"====================Bienvenido al cajero automático, {usuario}====================\n")

#Estado de la cuenta
if cuenta_bloqueada:
    print("Su cuenta está bloqueada. No puede realizar retiros.\n")
else:
    print(f"Su cuenta está activa. Puede realizar retiros.\n\n\
Saldo disponible: ${saldo_actual}\n\
Cuanto desea retirar?\n\
retiro: ${retiro}\n")
    if retiro <= 0:
        print("Monto inválido. El retiro debe ser mayor que 0.\n\n\
====================transacción finalizada====================\n")
    elif retiro > saldo_actual:
        print("Saldo insuficiente. No puede retirar más de lo que tiene en su cuenta.\n\n\
====================transacción finalizada====================\n")
    else:
        print(f"Retiro realizado con éxito.\n\
saldo retirado: ${retiro}\n\
saldo restante: ${saldo_restante}\n\n\
====================transacción finalizada====================\n")