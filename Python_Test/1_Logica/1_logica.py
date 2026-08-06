# ==========================================
#Ejercicio 1 — Sistema de compra
# ==========================================

name_producto = "teclado"
cantidad = 3
precio_original = 3600

precio_total = (precio_original * cantidad)
es_premium = True

if es_premium:
    print("======================== Compra premium ========================\n")
else:
    print("========================= Compra Nomal =========================\n")

print(f"\
Lista de productos:\n\
- {name_producto.capitalize()}.................................................UND: {cantidad}\n\
Precio original:.........................................${precio_original}\n")

if cantidad >= 3 and es_premium:
    und_descuento = precio_original * 0.15
    descuento = precio_total * 0.15
    precio_final = precio_total - descuento

    print(f"======================== Descuento del 15% ========================\n\
Descuento por unidad.....................................${und_descuento}\n\
Descuento Total aplicado.................................${descuento}\n\
Precio Final:............................................${precio_final}")
    
elif cantidad >= 3:
    und_descuento = precio_original * 0.10
    descuento = precio_total * 0.10
    precio_final = precio_total - descuento
    print(f"======================== Descuento del 10% ========================\n\
Descuento por unidad.....................................${und_descuento}\n\
Descuento Total aplicado.................................${descuento}\n\
Precio Final:............................................${precio_final}")
    
elif es_premium:
    und_descuento = precio_original * 0.05
    descuento = precio_total * 0.05
    precio_final = precio_total - descuento
    print(f"======================== Descuento del  5% ========================\n\
Descuento por unidad.....................................${und_descuento}\n\
Descuento Total aplicado.................................${descuento}\n\
Precio Final:............................................${precio_final}")
    
else:
    descuento = 0
    und_descuento = 0
    precio_final = precio_total
    print(f"======================== Descuento del  0% ========================\n\
Descuento por unidad.....................................${und_descuento}\n\
Descuento Total aplicado.................................${descuento}\n\
Precio Final:............................................${precio_final}")


# ==========================================
#
# ==========================================