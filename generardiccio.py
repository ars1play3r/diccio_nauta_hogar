# Nombre del archivo de salida
nombre_archivo = "diccionario_8_digitos.txt"

# Abrimos el archivo en modo escritura
with open(nombre_archivo, "w") as archivo:
    # Generamos todos los números de 8 dígitos (00000000 a 99999999)
    for numero in range(100_000_000):  # 0 a 99,999,999
        # Formateamos el número con 8 dígitos, rellenando con ceros a la izquierda
        combinacion = f"{numero:08d}"
        # Escribimos en el archivo
        archivo.write(combinacion + "\n")

print(f"✅ Diccionario generado: '{nombre_archivo}'")
print(f"📁 Total de combinaciones: 100,000,000")
print(f"📦 Tamaño estimado del archivo: ~900 MB")