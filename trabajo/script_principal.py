from vehiculo import Vehiculo
from brazo_robotico import BrazoRobotico
from operario import Operario

if __name__ == "__main__":
    auto = Vehiculo("V-001", "Sedán 2026", "Blanco", "En chasis", [])
    brazo = BrazoRobotico("RBT-99", "Ventosas de succión", 100, 35.5, False)
    tecnico = Operario("Carlos Pacheco", "EMP-123", "Ingeniero de Ensamblaje", False, 10)

    tecnico.iniciar_turno()
    tecnico.conectar_tablet()
    tecnico.mostrar_perfil()
    
    brazo.encender()
    
    tecnico.supervisar_robot(brazo)
    tecnico.mandar_instalar_pieza(brazo, auto, "Parabrisas Frontal")
    tecnico.aumentar_fatiga()
    
    auto.avanzar_estacion()
    auto.pintar("Rojo")
    auto.tocar_bocina()
    
    auto.mostrar_detalles()
    brazo.diagnosticar()
    
    brazo.apagar()
    tecnico.finalizar_turno()