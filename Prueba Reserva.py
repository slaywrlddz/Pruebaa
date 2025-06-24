reservas = []
stock = 20
def menu():
    print("TOTEM AUTOATENCIÓN RESERVA STRIKE")
    print("1.- Reservar zapatillas")
    print("2.- Buscar zapatillas reservadas")
    print("3.- Ver stock de reservas")
    print("4.- Salir")

def nombre_registrado(nombre):
    for r in reservas:
        if r["nombre"] == nombre:
            return True
    return False

def buscar_reserva_nombre(nombre):
        for r in reservas:
        if r["nombre"] == nombre:
            return r
        return None

def reservar_zapatillas():
     if len(reservas) >= stock:
          print("No hay stock disponible")
          return

nombre = input("Ingrese nombre de comprador: ")
if nombre_registrado(nombre):
    print("Error. Este nombre ya tiene una reserva registrada")


codigosecreto = input("Ingrese la palabra secreta para confirmar su reserva: ")
if codigosecreto != "EstoyEnListaDeReservas":
     print("Codigo secreto incorrecto, No se pudo realizar su reserva")

reservas.append({"Nombre", "Codigosecreto", "Vip";})
print("Reserva Realizada exitosamente.")

def buscar_reserva():
    nombre = input("Ingrese el nombre del comprador para buscar su reserva: ")
    reserva = buscar_reserva_nombre(nombre)
    if reserva is not None:
        print(f"Reserva encontrada para: {nombre}")
        if not reserva["vip"]:
            respuesta = input("¿Desea pagar un adicional por la reserva VIP? (s/n): ")
            if respuesta.lower() == 's':
                reserva["vip"] = True
                print("Reserva actualizada a VIP (2 pares de zapatillas).")
            else:
                print("No se realizó la actualización a VIP.")
        else:
            print("Este comprador ya tiene reserva VIP.")
    else:
        print("No se encontró ninguna reserva con ese nombre.")

def ver_stock():
    total_reservadas = len(reservas)
    restantes = stock - total_reservadas
    print(f"\nTotal de reservas realizadas: {total_reservadas}")
    print(f"Stock restante disponible: {restantes}")

def codigo():
     while True:
          opcion = input("Seleccione una opción (1-4): ")
          if opcion == 1:
            reservar_zapatillas()
          elif opcion == 2:
               buscar_reserva_nombre()
          elif opcion == 3:
               nombre_registrado()
          elif opcion == 4: 
               print("Programa terminado.")
               break
          else:
               print("Debe ingresar una opción válida!!")
               
                
#Tiene un error de if que puedo arreglarlo