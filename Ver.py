import Funciones as funciones
import Cambio as res
import json
def operaciones (nombre,dni,n_cuenta,pin):
    while True:
        cambio=funciones.cambios()
        if cambio== "ver saldo" or cambio=='2':
            try:
                with open (nombre+dni+n_cuenta+".txt", "r")as datos:
                    for line in datos:
                        try:
                            datosCuenta= json.loads(line.strip())
                            print(datosCuenta)
                        except:
                            print()
            except:
                print()
        elif cambio=='realizar deposito' or cambio=='1':
            ingreso=float(input('¿Cual es la cantidad que desea ingresar:'))
            with open (nombre+dni+n_cuenta+'.txt', 'r')as datos:
                for line in datos:
                    datosCuenta=json.loads(line.strip())
            funciones.ing(ingreso,nombre,dni,n_cuenta)
            importe=str(ingreso+datosCuenta)
            print('Tu saldo actual es de:'+importe)
            with open(nombre+dni+n_cuenta+'.txt', 'w')as datos:
                datos.write(importe)
        elif cambio == 'retirar dinero' or cambio=='3':
            while True:
                retiro = float(input('¿Que cantidad desea retirar?:'))
                with open (nombre+dni+n_cuenta+'.txt', 'r') as datos:
                    for line in datos:
                        datosCuenta= float(json.loads(line.strip()))
                    if retiro>datosCuenta and retiro!=0:
                        print ('no puedes retirar mas dinero del que tienes')
                    elif retiro<=datosCuenta or retiro==0:
                        importe= str(datosCuenta-retiro)
                        with open (nombre+dni+n_cuenta+'.txt', 'w') as datos:
                            datos.write(importe)
                        funciones.ret(retiro,nombre,dni,n_cuenta)
                        break
        elif cambio=='cambiar pin' or cambio=='4':
            res.nupin(nombre, dni, n_cuenta, pin)
        elif cambio=='Ver historial de transacciones' or cambio=='5':
            with open (nombre+dni+n_cuenta+'historial.txt', 'r') as historial:
                contenido=historial.read()
                print(contenido)
