from functools import wraps

def nom(funcion):
    @wraps (funcion)
    def env(*args, **kwargs):
        generador = funcion(*args, **kwargs)
        next(generador)
        return generador
    return env

@nom

def Planta(successor=None):
    while 1:
        cust = (yield)
        if cust.custtype == 'planta':
           print "Liquidando profesor de planta"
        elif successor is not None:
           successor.send(cust)

@nom
def Catedra(successor=None):
    while 1:
        cust = (yield)
        if cust.custtype == 'catedra':
           print "Liquidando profesor de catedra"
        elif successor is not None:
           successor.send(cust)

@nom
def Administrativo(successor=None):
    while 1:
        cust = (yield)
        if cust.custtype == 'administrativo':
           print "Liquidando administrativo"
        elif successor is not None:
           successor.send(cust)

@nom
def Monitor(successor=None):
    while 1:
        cust = (yield)
        if cust.custtype == 'monitor':
           print "Liquidando monitor"
        elif successor is not None:
           successor.send(cust)

@nom
def Default():
    while 1:
        cust = (yield)
        print "No existe '%s'" % cust.custtype

class IAprovador:
    revisa = Planta(Catedra(Administrativo(Monitor(Default()))))

    def __init__(self,custtype):
        self.custtype = custtype


    def Manejador(self):
        self.revisa.send(self)

if __name__ == '__main__':
    print "Ingrese el tipo de nomina"
    nomina = raw_input()
    nomina1 = IAprovador(nomina)
    nomina1.Manejador()
