class Vehiculo:
    def __init__(self, id_vehiculo, modelo, color, estado, piezas_instaladas):
        self._id_vehiculo = id_vehiculo
        self._modelo = modelo
        self._color = color
        self._estado = estado
        self._piezas_instaladas = piezas_instaladas

    def get_id_vehiculo(self): return self._id_vehiculo
    def get_modelo(self): return self._modelo
    def get_color(self): return self._color
    def get_estado(self): return self._estado
    def get_piezas_instaladas(self): return self._piezas_instaladas

    def set_id_vehiculo(self, id_v): self._id_vehiculo = id_v
    def set_modelo(self, mod): self._modelo = mod
    def set_color(self, col): self._color = col
    def set_estado(self, est): self._estado = est
    def set_piezas_instaladas(self, piezas): self._piezas_instaladas = piezas

    def encender_motor_prueba(self):
        print(f"🚗 {self._modelo}: Motor encendido para prueba.")

    def apagar_motor_prueba(self):
        print(f"🚗 {self._modelo}: Motor apagado.")

    def instalar_pieza(self, pieza):
        self._piezas_instaladas.append(pieza)
        print(f"🚗 {self._modelo}: Pieza '{pieza}' instalada.")

    def remover_pieza(self, pieza):
        if pieza in self._piezas_instaladas:
            self._piezas_instaladas.remove(pieza)
            print(f"🚗 {self._modelo}: Pieza '{pieza}' removida.")

    def avanzar_estacion(self):
        print(f"🚗 {self._modelo}: Avanzando a la siguiente estación de ensamblaje.")

    def pintar(self, nuevo_color):
        self.set_color(nuevo_color)
        print(f"🚗 {self._modelo}: Ha sido pintado de color {self._color}.")

    def tocar_bocina(self):
        print(f"🚗 {self._modelo}: ¡BEEP BEEP!")

    def verificar_ensamblaje(self):
        if len(self._piezas_instaladas) >= 3:
            self.set_estado("Completado")
        else:
            self.set_estado("En proceso")
        print(f"🚗 {self._modelo}: Estado actualizado a '{self._estado}'.")

    def emitir_alerta(self, mensaje):
        print(f"⚠️ ALERTA VEHÍCULO {self._id_vehiculo}: {mensaje}")

    def mostrar_detalles(self):
        print(f"🚗 INFO -> ID: {self._id_vehiculo} | Modelo: {self._modelo} | Color: {self._color} | Estado: {self._estado} | Piezas: {self._piezas_instaladas}")