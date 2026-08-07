# ==========================================
# Ejercicio 2 — Clasificación de estudiante
# ==========================================

Estudiante = "Carlos"
Matematicas = 4.2
Programacion = 4.8
Promedio = 0
Asistencia = 92

# Name
print(f"========================= INFORME ACADEMICO =========================\n\
                              {Estudiante}\n")

# Notas

print("Notas:\n\
>Matemáticas")

if Matematicas >= 4.5:
    print(f"Nota excelente: {Matematicas}\n")
elif Matematicas >= 3.5:
    print(f"Aprobado: {Matematicas}\n")
else:
    print(f"Reprobado: {Matematicas}\n")

print(">Programación")

if Programacion >= 4.5:
    print(f"Nota excelente: {Programacion}\n")
elif Programacion >= 3.5:
    print(f"Aprobado: {Programacion}\n")
else:
    print(f"Reprobado: {Programacion}\n")

# Promedio

Promedio = (Matematicas + Programacion) / 2
rendimiento_promedio = ""

if Promedio >= 4.5:
    rendimiento_promedio = f"Tienes un rendimiento superior de {Promedio}"
elif Promedio >= 3.5:
    rendimiento_promedio = f"Tienes un rendimiento promedio de {Promedio}"
else:
    rendimiento_promedio = f"Tienes un rendimiento mediocre de {Promedio}"

# Asistencia

rendimiento_asistencia = ""

if Asistencia >= 90:
    rendimiento_asistencia = f"Excelente del {Asistencia}%"
elif Asistencia >= 80:
    rendimiento_asistencia = f"Alta del {Asistencia}%"
elif Asistencia >= 70:
    rendimiento_asistencia = f"Aceptable del {Asistencia}%"
else:
    rendimiento_asistencia = f"Nefasta del {Asistencia}%"

# Resultado final

print("\n========================== RESULTADO FINAL ==========================")

if Asistencia < 70:
    print(f"Asistencia: {rendimiento_asistencia}")
    print("Resultado: Reprobado automáticamente por baja asistencia.")
else:
    print(f"{rendimiento_promedio} con una asistencia {rendimiento_asistencia}")