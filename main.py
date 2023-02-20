class Asiento:
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro
    def cambiarColor(self, color):
        colores = ["negro","blanco","rojo","verde","amarillo"]
        color.lower()
        if color in colores:
            self.color = color

class Auto:
    cantidadCreados = 0
    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro
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

class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro
    def cambiarRegistro(self, registro):
        self.registro = registro
    def asignarTipo(self, tipo):
        tipos=["electrico","gasolina"]
        tipo.lower()
        if tipo in tipos:
            self.tipo = tipo


