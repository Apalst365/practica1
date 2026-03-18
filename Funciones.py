import json
import Fun_sql as sql
import uuid

#valida si el dni es posible que exista usando el algoritmo real para calcular los dni
def valid_dni(dni):
    while True:
        long=len(dni)
        if long<9:
            try:
                if dni == 's':
                    return False
            except:
                print('error')
        else:
            if long == 9:
                try:
                    num=dni[0:8]
                    num=int(num)
                    div=num%23
                    tabla= {
                        0:'T', 1:'R', 2:'W', 3:'A', 4:'G', 5:'M',
                        6:'Y', 7:'F', 8:'P', 9:'D', 10:'X', 11:'B',
                        12:'N', 13:'J', 14:'Z', 15:'S', 16:'Q', 17:'V',
                        18:'H', 19:'L', 20:'C', 21:'K', 22:'E'
                    }
                    try:
                        if tabla[div] != dni[8:9]:
                            print('dni no valido')
                            return 'invalido'
                        elif tabla[div] == dni[8:9]:
                            return True
                    except:
                        print('error')
                except:
                    print('error')
            else:
                print (long)
                continue

#genera una cuenta con los datos que se piden aqui o genera los propios datos
def singup (): 
    print ('si quieres salir escribe "s"')   
    while True:
        dni=input("DNI:").strip()
        regreso=valid_dni(dni)
        if not regreso:
            return False
        elif regreso=='invalido':
            continue
        elif regreso:
            break
    nombre = input("Nombre:").strip()
    n_cuenta =str(uuid.uuid4())
    pin = input("Pin:").strip()
    ingreso= float(input("¿cuanto saldo desearia ingresar?:"))
    existe = False
    try:
        try:
            resultados=sql.extraer()
        except:
            print('error de seleccion')
        try:
            for fila in resultados:
                if (fila['dni']==dni):
                    existe= True
                    print('Ya dispones de una cuenta')
                    otra=input('¿Quieres crear otra?').strip()
                    if otra.lower() == 'si':
                        sql.insert_c(n_cuenta,pin,ingreso)
                        return True
                        
                else:
                    sql.insert_c(n_cuenta,pin,ingreso)
        except:
            print('error al crear usuario')
    except FileNotFoundError:
        print ('file not found')
    if not existe:
        sql.insert_c(n_cuenta,pin,ingreso)
        return True

#valida para que se de el inicio de sesion
def validar(dni, pin):
    try:
        with open("BaseDatos.txt", "r") as archivo:
            for linea in archivo:
                usuario = json.loads(linea)
                if (usuario["DNI"] == dni and usuario["pin"] == pin):
                    n_cuenta = usuario["n_cuenta"]
                    pin = usuario["pin"]
                    nombre = usuario["nombre"]
                    dni = usuario["DNI"]
                    return True, nombre, n_cuenta
                else:
                    print ('nombre o contraseña incorrectos')
        return False, None, None
    except:
        print('algo salio mal')

#inicia sesion
def login():
    while True:
        retroceso, dni, pin = pedir_datos()
        if retroceso:
            return True,None,None,None,None
        valid, nombre, n_cuenta= validar(dni, pin)
        if valid==True:
            print("Inicio de sesión exitoso.")
            return False,nombre,dni,n_cuenta,pin
        elif valid == False:
            print("Datos incorrectos. Inténtelo de nuevo.")

def pedir_datos():
    print ('si quieres salir escribe "s"')
    dni = input("dni:").strip()
    if dni=='s':
        return True, None, None
    pin = input("Pin:").strip()
    return False, dni, pin

def ver ():
    print ("1.-Realizar deposito")
    print("2.-Ver saldo")
    print("3.-Retirar dinero")
    print("4.-Cambiar pin")
    print("5.-Ver historial de transacciones")

def cambios():
    print ('Para ver opciones escribe "ver"')
    orden = input("¿Que desea?:").lower()
    if orden == 'ver':
        ver()
    return orden

def ing(ingreso,nombre,dni,n_cuenta):
    try:
        ingreso=str(ingreso)
        with open (nombre+dni+n_cuenta+'historial.txt', 'a') as historial:
            historial.write('+'+ingreso+'\n')
    except ValueError:
        print('la cantidad deve ir en numeros, ValueError')

def ret(retiro,nombre,dni,n_cuenta):
    try:
        retiro=str(retiro)
        with open (nombre+dni+n_cuenta+'historial.txt', 'a') as historail:
            historail.write('-'+retiro+'\n')
    except ValueError:
        print('la cantidad debe de ir en numero, ValueError')
