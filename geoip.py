import requests

def obtener_ubicacion(ip):
    url = f"(link unavailable)"
    response = requests.get(url)
    return response.json()

def main():
    print("-----------------------------↓")
    ip = input("Ingrese la dirección IP: ")
    ubicacion = obtener_ubicacion(ip)

    print("\033[1;34m\n======================================\033[0m")
    print("\033[1;34m Ubicación Geográfica \033[0m")
    print("\033[1;34m======================================\033[0m")

    print(f"\033[1;32mPaís:\033[0m {ubicacion.get('country', 'No disponible')}")
    print(f"\033[1;32mRegión:\033[0m {ubicacion.get('regionName', 'No disponible')}")
    print(f"\033[1;32mCiudad:\033[0m {ubicacion.get('city', 'No disponible')}")
    print(f"\033[1;32mLatitud:\033[0m {ubicacion.get('lat', 'No disponible')}")
    print(f"\033[1;32mLongitud:\033[0m {ubicacion.get('lon', 'No disponible')}")
    print(f"\033[1;32mCódigo Postal:\033[0m {ubicacion.get('zip', 'No disponible')}")
    print(f"\033[1;32mProveedor de Servicios de Internet (ISP):\033[0m {ubicacion.get('isp', 'No disponible')}")
    print(f"\033[1;32mOrganización:\033[0m {ubicacion.get('org', 'No disponible')}")
    print(f"\033[1;32mProveedor de Servicios de Internet (AS):\033[0m {ubicacion.get('as', 'No disponible')}")
    print(f"\033[1;32mDistrito:\033[0m {ubicacion.get('district', 'No disponible')}")
    print(f"\033[1;32mÁrea Metropolitana:\033[0m {ubicacion.get('metro', 'No disponible')}")
    print(f"\033[1;32mTipo de Conexión:\033[0m {ubicacion.get('connectionType', 'No disponible')}")
    print(f"\033[1;32mProveedor de Servicios Móviles:\033[0m {ubicacion.get('mobile', 'No disponible')}")

    print("\033[1;34m======================================\033[0m")

if __name__ == "__main__":
    main()
