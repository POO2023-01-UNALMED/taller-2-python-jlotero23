class Asiento:

    def __init__(self, color, precio, registro):
        self.registro=registro
        self.color=color
        self.precio=precio

    def cambiarColor(self,color):
        colores = ["negro","blanco","rojo","verde","amarillo"]
        color.lower()
        if color in colores:
            self.color=color

class Motor:

    def _init_(self, numeroCilindros, tipo, registro):
        self.registro=registro
        self.tipo=tipo
        self.numeroCilindros=numeroCilindros

    def cambiarRegistro(self, registro):
        self.registro=registro

    def asignarTipo(self, tipo):
        tipos=["electrico","gasolina"]
        tipo.lower()
        if tipo in tipos:
            self.tipo=tipo

class Auto:

    def __init__(self, modelo, precio, asientos, marca, motor, registro, cantidadCreados):
        self.modelo=modelo
        self.precio=precio
        self.asientos=asientos
        self.marca=marca
        self.motor=motor
        self.registro=motor
        self.registro=registro
        self.cantidadCreados=cantidadCreados

    def cantidadAsientos(self):
        cant=0
        for i in self.asientos:
            if i!= None:
                cant+=1
        return cant

    def verificarIntegridad(self):
        mensaje = "Las piezas no son originales"
        if self.registro==self.motor.registro:
            mensaje = "Auto original"
            for i in self.asientos:
                if i!=None:
                    if i.registro!=self.registro:
                        mensaje = "Las piezas no son originales"
        return mensaje

