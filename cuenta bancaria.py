import Funciones as funciones
import Ver as ver
while True:
    ti= input("¿Tiene ya una cuenta?").lower()
    if ti == "no":
        funciones.singup()
        continue
    elif ti== "si" or funciones.singup():
        try:
            denegacion,nombre,dni,n_cuenta,pin = funciones.login()
            if not denegacion:
                ver.operaciones(nombre,dni,n_cuenta,pin)
                break
            else:
                continue
        except:
            print ('Algo salio mal')
        continue
    else:
        print ("respuesta no valida")
