class Operario:
    def __init__(self, nombre, id_empleado, rol, tablet_conectada, fatiga):
        self._nombre = nombre
        self._id_empleado = id_empleado
        self._rol = rol
        self._tablet_conectada = tablet_conectada
        self._fatiga = fatiga

    def get_nombre(self): return self._nombre
    def get_id_empleado(self): return self._id_empleado
    def get_rol(self): return self._rol
    def get_tablet_conectada(self): return self._tablet_conectada
    def get_fatiga(self): return self._fatiga

    def set_nombre(self, nom): self._nombre = nom
    def set_id_empleado(self, id_emp): self._id_empleado = id_emp
    def set_rol(self, rol): self._rol = rol
    def set_tablet_conectada(self, tab): self._tablet_conectada = tab
    def set_fatiga(self, fat): self._fatiga = fat

    def iniciar_turno(self):
        print(f"👷 {self._nombre}: Iniciando turno como {self._rol}.")

    def finalizar_turno(self):
        print(f"👷 {self._nombre}: Turno finalizado. Buen descanso.")

    def conectar_tablet(self):
        self.set_tablet_conectada(True)
        print(f"👷 {self._nombre}: Tablet conectada a la red de la planta.")

    def desconectar_tablet(self):
        self.set_tablet_conectada(False)
        print(f"👷 {self._nombre}: Tablet desconectada.")

    def supervisar_robot(self, robot):
        print(f"👷 {self._nombre}: Supervisando al robot {robot.get_id_robot()}...")
        robot.diagnosticar()

    def mandar_instalar_pieza(self, robot, vehiculo, pieza):
        if self._tablet_conectada:
            print(f"👷 {self._nombre}: Ordenando a {robot.get_id_robot()} instalar {pieza}.")
            robot.tomar_pieza(pieza)
            robot.mover_posicion(10, 20, 5)
            vehiculo.instalar_pieza(pieza)
            robot.soltar_pieza()
            robot.consumir_bateria(10)
        else:
            print(f"👷 {self._nombre}: No puedo dar la orden, tablet desconectada.")

    def tomar_descanso(self):
        self.set_fatiga(0)
        print(f"👷 {self._nombre}: Descanso tomado. Nivel de fatiga restablecido a 0%.")

    def aumentar_fatiga(self):
        self.set_fatiga(self._fatiga + 15)
        if self._fatiga > 80:
            print(f"⚠️ {self._nombre} está muy fatigado ({self._fatiga}%). Necesita descanso.")

    def reportar_falla(self, mensaje):
        print(f"🚨 REPORTE DE {self._nombre} ({self._rol}): {mensaje}")

    def mostrar_perfil(self):
        conexion = "Conectado" if self._tablet_conectada else "Desconectado"
        print(f"👷 PERFIL -> {self._nombre} (ID: {self._id_empleado}) | Rol: {self._rol} | Fatiga: {self._fatiga}% | Tablet: {conexion}")