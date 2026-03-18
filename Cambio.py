import json

def tupin():#pregunta el pin actual
    pun=input('¿Cual es el pin actual?')
    return pun

def recpin(nombre, n_cuenta, dni):
    print('Escribe tu nombre, n-cuenta y tu dni asocciado a tu cuenta en ese orden (presiona enter despues de introducir un dato)')
    comprov_nom=input()
    comprov_ncuen=input()
    comprov_dni=input()
    if comprov_nom==nombre and comprov_ncuen==n_cuenta and comprov_dni==dni:
        return True
    elif comprov_nom!=nombre and comprov_ncuen!=n_cuenta and comprov_dni!=dni:
        return False

def nupin(nombre, dni, n_cuenta, pin):
    while True:
        pun=tupin()
        if pun==pin:
            igual(pin, nombre, dni, n_cuenta)
            break
        elif pun!=pin:
            olv=input('¿Has olvidado la contraseña?')
            if olv == 'si':
                valid=recpin(nombre, n_cuenta, dni)
                if valid:
                    igual(pin, nombre, dni, n_cuenta)
            elif olv=='no':
                print('contraseña inocrrecta')
                continue
            continue
        continue           

def ndat():
    npin=input('Escribe el nuevo pin:')
    return npin

def igual(pin, nombre, dni, n_cuenta):#si no es igual el pin antiguo y el nuevo se modifica
    npin=ndat()
    if npin==pin:
        print('No puedes poner la misma contraseña que tenias')
        return None
    elif npin!=pin:
        modBase=modpin(npin,nombre,dni,n_cuenta)
        sino=input('¿Tu nuevo pin es:'+npin+'?').lower()
        if sino=='si':
            modBase = modpin(npin, nombre, dni, n_cuenta)
            print('Se ha cambiado la contraseña')
            return modBase
        return modBase, None
    
def modpin(npin,nombre,dni,n_cuenta):
    while True:
        with open ('BaseDatos.txt', 'r')as a:
            lin=a.readlines()
        n_lineas= []
        for line in lin:
            dat=json.loads(line.strip())#tranforma la linea en un diccionario y con el .strip quita espacios y saltos de linea
            if dat['nombre'] == nombre and dat['DNI'] == dni and dat['n_cuenta'] == n_cuenta:
                dat['pin']=npin#modifica el pin
            n_lineas.append(json.dumps(dat)+'\n')
        with open ('BaseDatos.txt', 'w')as a:
            a.writelines(n_lineas)#escribe los cambios
        return n_lineas
    
