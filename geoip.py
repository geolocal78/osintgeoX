import requests
 
  def obtener_ubicacion(ip):
      url = f"http://ip-api.com/json/{ip}"
      response = requests.get(url)
      return response.json()
 
  def main():
      print("-----------------------------↓")
     ip = input("Ingrese la dirección IP: ")
     ubicacion = obtener_ubicacion(ip)

     print("\033[1;34m\n======================================\033[0
     print("\033[1;34m Ubicación Geográfica \033[0m")
     print("\033[1;34m======================================\033[0m"

     print(f"\033[1;32mPaís:\033[0m {ubicacion.get('country', 'No di
     print(f"\033[1;32mRegión:\033[0m {ubicacion.get('regionName', '
     print(f"\033[1;32mCiudad:\033[0m {ubicacion.get('city', 'No dis
     print(f"\033[1;32mLatitud:\033[0m {ubicacion.get('lat', 'No dis
     print(f"\033[1;32mLongitud:\033[0m {ubicacion.get('lon', 'No di
     print(f"\033[1;32mCódigo Postal:\033[0m {ubicacion.get('zip', '
     print(f"\033[1;32mProveedor de Servicios de Internet (ISP):\033
     print(f"\033[1;32mOrganización:\033[0m {ubicacion.get('org', 'N
     print(f"\033[1;32mProveedor de Servicios de Internet (AS):\033[
     print(f"\033[1;32mPaís:\033[0m {ubicacion.get('country', 'No di
     print(f"\033[1;32mRegión:\033[0m {ubicacion.get('regionName', '
     print(f"\033[1;32mCiudad:\033[0m {ubicacion.get('city', 'No dis
     print(f"\033[1;32mLatitud:\033[0m {ubicacion.get('lat', 'No dis
     print(f"\033[1;32mLongitud:\033[0m {ubicacion.get('lon', 'No di
     print(f"\033[1;32mCódigo Postal:\033[0m {ubicacion.get('zip', '
     print(f"\033[1;32mProveedor de Servicios de Internet (ISP):\033
     print(f"\033[1;32mOrganización:\033[0m {ubicacion.get('org', 'N
     print(f"\033[1;32mProveedor de Servicios de Internet (AS):\033[
     print(f"\033[1;32mDistrito:\033[0m {ubicacion.get('district', '
     print(f"\033[1;32mÁrea Metropolitana:\033[0m {ubicacion.get('me
     print(f"\033[1;32mTipo de Conexión:\033[0m {ubicacion.get('conn
     print(f"\033[1;32mProveedor de Servicios Móviles:\033[0m {ubica
     print("\033[1;34m======================================\033[0m\

 if __name__ == "__main__":
     main()
