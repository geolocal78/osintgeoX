import webbrowser

# Define las URLs
urls = {
    1: "https://minosis.com",
    2: "https://www.indec.gob.ar",
    3: "https://www.afip.gob.ar",
    4: "https://www.bcra.gob.ar",
    }

# Muestra el menú de opciones
print("Seleccione una opción:")
for key, value in urls.items():
    print(f"{key}: {value}")

# Pide al usuario que seleccione una opción
opcion = int(input("Ingrese el número de la opción: "))

# Abre la URL seleccionada
webbrowser.open(urls[opcion])
