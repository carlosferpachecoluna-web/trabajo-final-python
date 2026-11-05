class BrazoRobotico:
    def __init__(self, id_robot, herramienta, bateria, temperatura, encendido):
        self._id_robot = id_robot
        self._herramienta = herramienta
        self._bateria = bateria
        self._temperatura = temperatura
        self._encendido = encendido

    def get_id_robot(self): return self._id_robot
    def get_herramienta(self): return self._herramienta
    def get_bateria(self): return self._bateria
    def get_temperatura(self): return self._temperatura
    def get_encendido(self): return self._encendido

    def set_id_robot(self, id_r): self._id_robot = id_r
    def set_herramienta(self, herr): self._herramienta = herr
    def set_bateria(self, bat): self._bateria = bat
    def set_temperatura(self, temp): self._temperatura = temp
    def set_encendido(self, enc): self._encendido = enc

    def encender(self):
        self.set_encendido(True)
        print(f"🤖 Robot {self._id_robot}: Iniciando sistemas...")

    def apagar(self):
        self.set_encendido(False)
        print(f"🤖 Robot {self._id_robot}: Sistemas apagados.")

    def mover_posicion(self, eje_x, eje_y, eje_z):
        print(f"🤖 Robot {self._id_robot}: Moviendo coordenadas a (X:{eje_x}, Y:{eje_y}, Z:{eje_z}).")

    def tomar_pieza(self, pieza):
        print(f"🤖 Robot {self._id_robot}: Sujetando la pieza '{pieza}' con {self._herramienta}.")

    def soltar_pieza(self):
        print(f"🤖 Robot {self._id_robot}: Liberando pieza.")

    def cambiar_herramienta(self, nueva_herramienta):
        self.set_herramienta(nueva_herramienta)
        print(f"🤖 Robot {self._id_robot}: Herramienta cambiada a '{self._herramienta}'.")

    def recargar_bateria(self):
        self.set_bateria(100)
        print(f"🤖 Robot {self._id_robot}: Batería recargada al 100%.")

    def consumir_bateria(self, cantidad):
        self.set_bateria(self._bateria - cantidad)

    def enfriar_sistema(self):
        self.set_temperatura(30.0)
        print(f"🤖 Robot {self._id_robot}: Sistema refrigerado. Temperatura: {self._temperatura}°C.")

    def diagnosticar(self):
        estado = "ON" if self._encendido else "OFF"
        print(f"🤖 DIAGNÓSTICO -> {self._id_robot} | {estado} | Bat: {self._bateria}% | Temp: {self._temperatura}°C | Herr: {self._herramienta}")