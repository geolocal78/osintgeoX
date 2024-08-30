import os
  # Agrega tu nombre aquí
  nombre = r"Aaron"
  def menu():
     print(" _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
     print("|                                 |")
     print("|                                 |")      print("|                                 |")
     print("|                                 |")
     print("|                                 |")
     print("|                                 |")
     print("|__ᴀᴀʀᴏɴ_ ___ __ _ _ _ _ _ _ _ _ _|")

     nombre = "Aaron"
     print(f"\033[1;34m¡Hola,usuario! Seleccione una herramienta de
     print("")
     print("")
     print("➣")
     print("\033[1;34mSeleccione una herramienta de geolocalización:
     print("")
     print("➣")
     print("\033[1;32m1. PhoneInfoga - Información de teléfonos\033[
     print("")
     print("")
     print("➣")
     print("\033[1;33m2. Informes - Generador de informes\033[0m")
     print("")
     print("")
     print("➣")
     print("\033[1;35m3. GeoIP - Localización por IP\033[0m")
     print("")
     print("")
     print("➣")
     opcion = input("\033[1;36mIngrese el número de la opción: \033[

     if opcion == "1":
         os.system("python phoneinfoga")
     elif opcion == "2":
         os.system("python links.py")
     elif opcion == "3":
         os.system("python geoip.py")
     else:
         print("\033[1;31mOpción inválida. Por favor, seleccione una

 while True:
     menu()
