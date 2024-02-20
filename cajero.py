#Crear programa de cajero automatico. Opciones: Retiro y deposito
#Todas las transacciones registrarlas en un archivo de texto
#Perfil de Admin. Solo se le dara opcion para revisar el log de transacciones


#Esto para obtener la fecha y hora de transaccion
from datetime import datetime

class Cajero:

    #Siempre se iniciara con 0 en el saldo
    saldo = 0

    def opcionesCajero(self):
        while True:
            print("\nCAJERO AUTOMATICO\n")
            print("(1) Retiro")
            print("(2) Deposito")
            print("(3) Consulta de saldo")
            print("(4): Salir")

            opcion = input()
            if opcion not in ["1","2","3","4"]:
                print("\nDebe ingresar una opcion valida")
                continue
            elif opcion == "4":
                break
            elif opcion == "1":
                self.retiro()
            elif opcion == "2":
                self.ingresarMonto("depositar")
            elif opcion == "3":
                print(f"\nSu saldo es de: ${self.saldo}")


    def retiro(self):
        listaMontos = ["5000","10000","15000","20000","50000"]
        while True:
            print("\nRETIRO\n")
            print("(1) 5000")
            print("(2) 10000")
            print("(3) 15000")
            print("(4) 20000")
            print("(5) 50000")
            print("(6) Otro monto")
            print("(7) Volver")

            opcionRetiro = input()
            if opcionRetiro not in ["1","2","3","4","5","6","7"]:
                print("\nDebe ingresar una opcion valida")
                continue
            elif opcionRetiro == "7":
                break
            elif opcionRetiro != "6":
                montoRetiro = listaMontos[int(opcionRetiro) - 1]
                if self.saldo < int(montoRetiro):
                    print("\nNo tiene suficiente saldo para realizar esta operacion")
                else:
                    self.saldo -= int(montoRetiro)
                    self.escribirRegistro("RETIRO",montoRetiro)
                    break
            else:
                self.ingresarMonto("retirar")
                break

    
    def ingresarMonto(self,operacion):
        while True:
            print(f"\nIngrese monto a {operacion}")
            print("(q) Volver")
            montoIngreso = input()

            if(montoIngreso.lower() == "q"):
                break
            else:
                try:
                    montoIngreso = float(montoIngreso)
                    if montoIngreso < 0:
                        print("\nNo puede ingresar montos negativos")
                    elif montoIngreso == 0:
                        print("\nDebe ingresar un monto mayor a cero (0)")
                    else:
                        if operacion == "retirar":
                            operacion = "RETIRO"
                            if self.saldo < montoIngreso:
                                print("\nNo tiene suficiente saldo para realizar esta operacion")
                            else:
                                self.saldo -= montoIngreso
                        else:
                            operacion = "DEPOSITO"
                            self.saldo += montoIngreso

                        self.escribirRegistro(operacion,montoIngreso)
                        break
                except:
                    print("\nDebe ingresar un monto valido")
                    continue


    def getFechaYHora(self):
        objFecha = datetime.now()

        # dd/mm/YY H:M:S
        fechaYHora = objFecha.strftime("%d/%m/%Y, a las %H:%M:%S")
        return fechaYHora
    
    def escribirRegistro(self,operacion,monto):
        fecha = self.getFechaYHora()

        try:
            with open("registroTransacciones.txt","a") as file:
                file.write(f"\n{operacion} por ${monto} realizado el {fecha}")
            print("\nOPERACION REALIZADA CON EXITO")
        except:
            print("\nOcurrio un error al registrar la operacion en el registro de transacciones")
                                

class AdminCajero(Cajero):

    def opcionesCajero(self):
        while True:
            print("\nCAJERO AUTOMATICO (ADMIN)\n")
            print("(1) Revisar registro de transacciones")
            print("(2) Eliminar registro de transacciones")
            print("(3) Salir")

            opcionAdmin = input()
            if opcionAdmin not in ["1","2","3"]:
                print("\nDebe ingresar una opcion valida")
                continue
            elif opcionAdmin == "3":
                break
            elif opcionAdmin == "1":
                print("REGISTRO DE TRANSACCIONES DEL CAJERO AUTOMATICO\n")
                try:
                    with open("registroTransacciones.txt","r") as file:
                        if(file.read(1)):
                            for transaccion in file.readlines():
                                print(f"-{transaccion.strip()}")
                        else:
                            print("-NO HAY REGISTRO DE TRANSACCIONES")
                except:
                    print("\nOcurrio un error al leer el registro de transacciones")
            elif opcionAdmin == "2":
                while True:
                    print("\nEsta seguro de que quiere eliminar el registro de transacciones?")
                    print("(Y) Si")
                    print("(N) No")
                    opcionEliminar = input()
                    if opcionEliminar.upper() not in ["Y","N"]:
                        print("\nDebe ingresar una opcion valida")
                        continue                        
                    elif opcionEliminar.upper() == "Y":
                        try:
                            with open("registroTransacciones.txt","w") as file:
                                file.write("")
                            print("\n-Se han eliminado los registros de transacciones")
                        except:
                            print("\nOcurrio un error al eliminar los registros de transacciones")
                    break


while True:
    print("\n(1) Usuario normal")
    print("(2) Admin")
    print("(3) Salir")

    opcionInicio = input()
    if opcionInicio not in ["1","2","3"]:
        print("\nDebe ingresar una opcion valida")
        continue
    elif opcionInicio == "3":
        break
    elif opcionInicio == "1":
        usuario = Cajero()
        usuario.opcionesCajero()
    else:
        admin = AdminCajero()
        admin.opcionesCajero()  