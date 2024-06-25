import os
os.system("cls")
Dat_1 = []
Dat_2 = []
pat= []
marca= []
fecha_registro = []


while True:
    try:
        Opc_menu = int(input("Seleccione una opcion:\n 1) Grabar\n 2) Buscar \n3) Certificados \n 4) salir \nSeleccione: "))
        if Opc_menu == 1 : 
            print("Ponga sus datos")
            Dat_1 = input("Nombre y apelliido: ")
            Dat_2 = input("Run: ")
            print("Seleccione un Vehiculo")
            opc_vehiculo = int(input("Tipos de Vehiculo: \n1) Automovil \n2)Camion \n3) Camioneta \n4) Moto\nSeleccione una opcion: "))
            if opc_vehiculo == 1 :
                print("Escoja una patente")
                pat = input("Su patente debe llevar 4 letras (excepto M,N,Ñ), seguido de 2 numeros")
                
                print("¿Que marca desea adquirir")
                marca = input("Ingrese una marca (mayor a 2 caracteres)")
              
               
                
                        
            elif opc_vehiculo == 2:
                print("Escoja una patente")
                pat = input("Su patente debe llevar 4 letras (excepto M,N,Ñ), seguido de 2 numeros")
                
                print("¿Que marca desea adquirir")
                marca = input("Ingrese una marca (mayor a 2 caracteres)")
              
               
                
            elif opc_vehiculo == 3:
                print("Escoja una patente")
                pat = input("Su patente debe llevar 4 letras (excepto M,N,Ñ), seguido de 2 numeros")
                
                print("¿Que marca desea adquirir")
                marca = input("Ingrese una marca (mayor a 2 caracteres)")
              
                
            elif opc_vehiculo == 4:
                print("Escoja una patente")
                pat = input("Su patente debe llevar 4 letras (excepto M,N,Ñ), seguido de 2 numeros")
                
                print("¿Que marca desea adquirir")
                marca = input("Ingrese una marca (mayor a 2 caracteres)")
              
                
        elif Opc_menu == 2 :
            print("Ingrese patente")
            patente = input(":")
            print (f"Sus datos son\n Nombre:{Dat_1}\nRun:{Dat_2}\nPatente:{pat}\nMarca:{marca}\nFecha de registro:{fecha_registro}\n gracias por adquirir en Auto Seguro :D")
        elif Opc_menu == 3:
            print("Certificados")
            print(f"Sus datos son\n Nombre:{Dat_1}\nRun:{Dat_2}\nPatente:{pat}\nMarca:{marca}\nFecha de registro:{fecha_registro}")
        elif Opc_menu == 4 :
            print("Ha salido del programa...")
            break
        else:
            print("Opcion invalida")
    except:
        print("error")
