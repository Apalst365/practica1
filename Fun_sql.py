import mysql.connector as sql
from datetime import date
from dateutil.relativedelta import relativedelta

#iniciar conexion con la base de datos
def conex():
    try:
        db=sql.connect(
        host='localhost',
        user='bancario',
        password='2y#l*$0l#2&!928@qEG6@',
        database='credenciales'
        )
        return True,db
    except:
        print('error al conectarse a la base de datos')

#insertar datos en la tabla usuario
def insert_u(nombre,dni): 
    conectado,db=conex()
    if conectado:
        try:
            datos_usuario=(dni,nombre)
            cursor=db.cursor()
            cursor.execute(
                'USE CREDENCIALES;'
            )
            cursor.execute(
                'INSERT INTO USUARIO(DNI,NOMBRE) VALUES (%s,%s)',
                datos_usuario
            )
        except sql.Error:
            print('error sql')
            print (f'INSERT INTO USUARIO(dni,nombre) VALUES {datos_usuario}')   
        try:       
            db.commit() 
        except:
            print('error a la hora de guardar datos')

#insertar datos en la tabla de cuenta
def insert_c(n_cuenta,pin,ingreso):
    conectado,db=conex()
    if conectado:
        try:
            hoy=date.today()
            caducidad=str(hoy+relativedelta(years=+10))
            datos_cuenta=(n_cuenta,pin,caducidad,ingreso)
            cursor=db.cursor()
            cursor.execute(
                'USE CREDENCIALES;'
            )
            cursor.execute(
                'INSERT INTO HISTORIAL()'
            )
            cursor.execute(
                'USE CREDENCIALES;'
            )                        
            cursor.execute(
                'INSERT INTO CUENTAS(N_CUENTA,PIN,F_CADUCIDAD,SALDO) VALUES (%s,%s,%s,%s)',
                datos_cuenta
            )
        except sql.Error:
            print('error sql')
            print (f'INSERT INTO cuentas(N_CUENTA,PIN,F_CADUCIDAD,SALDO) VALUES {datos_cuenta}')
        try:       
            db.commit() 
        except:
            print('error a la hora de guardar datos')

#extraer datos de la base de datos para la validacion
def extraer():
    conectado,db=conex()
    if conectado:
        try:
            cursor=db.cursor()
            cursor.execute('SELECT * FROM cuentas')
            datos=cursor.fetchall()
            resultados=[]
            for fila in datos:
                bd_n_cuenta= fila[0]
                bd_nombre=fila[1]
                bd_pin=fila[2]
                bd_dni=fila[3]
                resultados.append({
                    'dni':bd_dni,
                    'n_cuenta':bd_n_cuenta,
                    'nombre':bd_nombre,
                    'pin':bd_pin
                    })
            return resultados
        except:
            print('error en entrar')
