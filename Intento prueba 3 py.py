import os
import random

os.system("cls")

tipo_vehiculos = ["Automovil", "Moto", "Camioneta", "Camion"]
vehiculos_registrados = {}

def Grabar_vehiculo():
    while True:
        try:
            datos_user = input("Ingrese Su nombre y Apellido\n")
            run_user = input("Ingrese su run\n")
            print(f"Escoja el tipo de vehiculo: \n{tipo_vehiculos}")
            opc_tipo_vehiculo = input()
            if opc_tipo_vehiculo not in tipo_vehiculos:
                print("No se encuentra el tipo de vehiculo")
                continue
            fecha_registro = input("Ingrese fecha de registro dd/mm/aaaa\n")
            marca = input("Escriba la marca que desea (debe incluir de 3 a 16 caracteres)\n")
            if len(marca) < 3 or len(marca) > 16:
                print("Escoja una marca valida")
                continue
            patente = input("Ingrese patente (son 6 caracteres), esta no puede llevar las letras M, Ñ y N, y tambien debe llevar 2 numeros.\n").upper()
            if len(patente) > 6 or "Ñ" in patente or "M" in patente or "N" in patente:
                print("Patente invalida")
                continue
            if patente in vehiculos_registrados:
                print("Patente ya existe, ingrese una patente diferente")
                continue
            
            precio = random.randint(5000000, 25000000)
            
            vehiculos_registrados[patente] = {
                "datos_user": datos_user,
                "run_user": run_user,
                "opc_tipo_vehiculo": opc_tipo_vehiculo,
                "fecha_registro": fecha_registro,
                "marca": marca,
                "precio": precio
            }
            
            print("Vehiculo registrado con exito!")
            return
        except:
            print("Error al registrar vehiculo")

def Buscar_patente():
    pat_buscar = input("Ingrese patente que ya este registrada en el sistema\n")
    #Para poder ingresar a la patente debe escribirla pero con mayuscula
    if pat_buscar in vehiculos_registrados:
        vehiculo = vehiculos_registrados[pat_buscar]
        print("Vehiculo encontrado!")
        print("Los datos de su vehiculo son:")
        print(F"Nombre y apellido: {vehiculo['datos_user']}")
        print(F"Run: {vehiculo['run_user']}")
        print(F"Tipo de vehiculo: {vehiculo['opc_tipo_vehiculo']}")
        print(F"Fecha de registro: {vehiculo['fecha_registro']}")
        print(F"Marca: {vehiculo['marca']}")
        print(F"Patente: {pat_buscar}")
        print(F"Precio: ${vehiculo['precio']}")
    else:
        print("Patente no encontrada")


def salida_del_programa():
    while True:
         opc_salida = input("¿Desea salir del programa?\n ").lower()
         if opc_salida == "si":
            print("Ha salido del sistema..")
            break
            

         elif opc_salida == "no":
            continue
         else:
            print("Opción inválida. Por favor, ingrese 'i' o 'no'.")
    


              
              
        
    

print('Bienvenido a "Auto Seguro"')
while True:
    try:
        opc_menu = int(input("Seleccione una opcion\n1)GRABAR\n2)BUSCAR PATENTE\n3)REGISTRO\n4)SALIR\n"))
        if opc_menu == 1:
            Grabar_vehiculo()
        elif opc_menu == 2:
            Buscar_patente()
        elif opc_menu == 4:
            salida_del_programa()
            break
    except:
        print("Error al seleccionar opcion")