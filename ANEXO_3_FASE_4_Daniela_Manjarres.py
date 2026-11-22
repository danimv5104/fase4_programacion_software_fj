"""
UNIVERSIDAD NACIONAL ABIERTA Y A DISTANCIA (UNAD)
Curso: Programación - Fase 4 (Componente Práctico)
Estudiante: Daniela Manjarres
Grupo: 153
Sistema: Gestión de Servicios y Reservas "Software FJ"
"""
import os
import logging
from abc import ABC, abstractmethod
from datetime import datetime

# ==============================================================================
# 1. RUTA ABSOLUTA PARA EL ARCHIVO DE LOGS
# Garantiza que 'sistema_manjarres.log' se guarde SIEMPRE dentro de esta carpeta.
# ==============================================================================
DIRECTORIO_ACTUAL = os.path.dirname(os.path.abspath(__file__))
RUTA_LOG = os.path.join(DIRECTORIO_ACTUAL, 'sistema_manjarres.log')

logging.basicConfig(
    filename=RUTA_LOG,
    level=logging.INFO,
    format='%(asctime)s | %(levelname)s | %(message)s',
    encoding='utf-8'
)
# ==============================================================================
# 1. CONFIGURACIÓN DEL SISTEMA DE REGISTRO DE EVENTOS (LOGS)
# Archivo exclusivo: sistema_manjarres.log
# ==============================================================================
logging.basicConfig(
    filename='sistema_manjarres.log',
    level=logging.INFO,
    format='%(asctime)s | %(levelname)s | %(message)s',
    encoding='utf-8'
)

# ==============================================================================
# 2. JERARQUÍA DE EXCEPCIONES PERSONALIZADAS
# ==============================================================================
class ErrorBaseSoftwareFJ(Exception):
    """Excepción raíz del sistema Software FJ."""
    pass

class ValidacionClienteError(ErrorBaseSoftwareFJ):
    """Se genera cuando los datos del cliente violan las reglas de negocio."""
    pass

class ValidacionServicioError(ErrorBaseSoftwareFJ):
    """Se genera ante parámetros inválidos en la creación de un servicio."""
    pass

class GestionReservaError(ErrorBaseSoftwareFJ):
    """Se genera ante inconsistencias en el proceso de reserva."""
    pass


# ==============================================================================
# 3. ENCAPSULACIÓN: CLASE CLIENTE
# ==============================================================================
class ClienteSoftwareFJ:
    def __init__(self, cedula: str, nombre_completo: str, email: str):
        self.cedula = cedula
        self.nombre_completo = nombre_completo
        self.email = email

    @property
    def cedula(self) -> str:
        return self._cedula

    @cedula.setter
    def cedula(self, valor: str):
        if not valor or not str(valor).strip():
            raise ValidacionClienteError("La cédula o identificación no puede estar vacía.")
        self._cedula = str(valor).strip()

    @property
    def nombre_completo(self) -> str:
        return self._nombre_completo

    @nombre_completo.setter
    def nombre_completo(self, valor: str):
        if not valor or not str(valor).strip():
            raise ValidacionClienteError("El nombre completo del cliente es obligatorio.")
        self._nombre_completo = str(valor).strip()

    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, valor: str):
        if "@" not in str(valor) or "." not in str(valor):
            raise ValidacionClienteError(f"Formato de correo electrónico inválido: '{valor}'")
        self._email = str(valor).strip()

    def obtener_resumen(self) -> str:
        return f"Cliente ID: {self._cedula} | {self._nombre_completo} ({self._email})"


# ==============================================================================
# 4. ABSTRACCIÓN Y HERENCIA: CLASE BASE ABSTRACTA Y SUBCLASES DE SERVICIO
# ==============================================================================
class ServicioBase(ABC):
    def __init__(self, codigo_servicio: str, descripcion: str, tarifa_base: float):
        self.codigo_servicio = codigo_servicio
        self.descripcion = descripcion
        self.tarifa_base = tarifa_base

    @abstractmethod
    def calcular_costo_total(self) -> float:
        """Polimorfismo: Cada subclase calcula el costo final según sus reglas."""
        pass

    def __str__(self):
        return f"[{self.codigo_servicio}] {self.descripcion} (Tarifa Base: ${self.tarifa_base:,.2f})"


# Subclase 1: Reserva de Sala de Conferencias
class SalaReuniones(ServicioBase):
    def __init__(self, codigo: str, desc: str, tarifa_base: float, horas_uso: int, incluye_catering: bool = False):
        super().__init__(codigo, desc, tarifa_base)
        if horas_uso <= 0:
            raise ValidacionServicioError("La cantidad de horas debe ser mayor a cero.")
        self.horas_uso = horas_uso
        self.incluye_catering = incluye_catering

    def calcular_costo_total(self) -> float:
        costo_horas = self.tarifa_base * self.horas_uso
        adicional_catering = 40000.0 if self.incluye_catering else 0.0
        return costo_horas + adicional_catering


# Subclase 2: Alquiler de Equipos Tecnológicos
class EquipoTecnologico(ServicioBase):
    def __init__(self, codigo: str, desc: str, tarifa_base: float, dias_alquiler: int, costo_seguro: float = 25000.0):
        super().__init__(codigo, desc, tarifa_base)
        if dias_alquiler <= 0:
            raise ValidacionServicioError("Los días de alquiler deben ser mínimo 1.")
        self.dias_alquiler = dias_alquiler
        self.costo_seguro = costo_seguro

    def calcular_costo_total(self) -> float:
        return (self.tarifa_base * self.dias_alquiler) + self.costo_seguro


# Subclase 3: Asesoría Técnica Especializada
class ConsultoriaEspecializada(ServicioBase):
    def __init__(self, codigo: str, desc: str, tarifa_base: float, sesiones: int, es_remota: bool = True):
        super().__init__(codigo, desc, tarifa_base)
        if sesiones <= 0:
            raise ValidacionServicioError("Debe programar al menos 1 sesión de asesoría.")
        self.sesiones = sesiones
        self.es_remota = es_remota

    def calcular_costo_total(self) -> float:
        subtotal = self.tarifa_base * self.sesiones
        descuento_remoto = subtotal * 0.10 if self.es_remota else 0.0
        return subtotal - descuento_remoto


# ==============================================================================
# 5. CLASE RESERVA Y GESTOR CENTRAL (Control de Excepciones)
# ==============================================================================
class ReservaEmpresarial:
    def __init__(self, folio: str, cliente: ClienteSoftwareFJ, servicio: ServicioBase):
        self.folio = folio
        self.cliente = cliente
        self.servicio = servicio
        self.fecha_registro = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.total_apagar = servicio.calcular_costo_total()

    def generar_comprobante(self) -> str:
        return f"Folio #{self.folio} | Fecha: {self.fecha_registro} | {self.cliente.nombre_completo} | Servicio: {self.servicio.descripcion} | Total: ${self.total_apagar:,.2f}"


class ControladorSoftwareFJ:
    def __init__(self):
        self.directorio_clientes = []
        self.catalogo_servicios = []
        self.historial_reservas = []

    def alta_cliente(self, cedula: str, nombre: str, email: str):
        try:
            nuevo_cliente = ClienteSoftwareFJ(cedula, nombre, email)
        except ValidacionClienteError as err:
            logging.error(f"Error al registrar cliente [{cedula}]: {err}")
            print(f"  ❌ Requisito no cumplido: {err}")
            return None
        else:
            self.directorio_clientes.append(nuevo_cliente)
            logging.info(f"Cliente dado de alta exitosamente: {nuevo_cliente.obtener_resumen()}")
            print(f"  ✅ Registrado: {nuevo_cliente.obtener_resumen()}")
            return nuevo_cliente
        finally:
            logging.info(f"Finalizó el proceso de alta para el cliente ID: {cedula}")

    def procesar_reserva(self, folio: str, cliente: ClienteSoftwareFJ, servicio: ServicioBase):
        try:
            if cliente is None:
                raise GestionReservaError("No se puede vincular una reserva a un cliente inexistente.")
            if servicio is None:
                raise GestionReservaError("El servicio seleccionado no es válido.")

            reserva = ReservaEmpresarial(folio, cliente, servicio)
        except GestionReservaError as err:
            logging.error(f"Fallo al emitir la reserva #{folio}: {err}")
            print(f"  ❌ Error en Reserva: {err}")
            return None
        else:
            self.historial_reservas.append(reserva)
            logging.info(f"Reserva registrada satisfactoriamente: {reserva.generar_comprobante()}")
            print(f"  ✅ Reserva Procesada: {reserva.generar_comprobante()}")
            return reserva
        finally:
            logging.info(f"Finalizó el intento de procesamiento de la reserva #{folio}")


# ==============================================================================
# 6. SIMULACIÓN DE 10 OPERACIONES (Demostración de Estabilidad)
# ==============================================================================
def ejecutar_pruebas_sistema():
    print("=" * 80)
    print("    SISTEMA INTEGRAL SOFTWARE FJ - EVALUACIÓN FASE 4 (DANIELA MANJARRES)    ")
    print("=" * 80)

    gestor = ControladorSoftwareFJ()

    # Caso 1 (Correcto): Registrar Cliente 1
    print("\n[Operación 1/10] Alta de Cliente Válido")
    cli1 = gestor.alta_cliente("1098765432", "Daniela Manjarres", "daniela.manjarres@unad.edu.co")

    # Caso 2 (Error Controlado): Registrar Cliente con Email Erróneo
    print("\n[Operación 2/10] Alta de Cliente con Email Sin Dominio")
    cli_bad = gestor.alta_cliente("1098765433", "Carlos Gómez", "carlos_sin_correo")

    # Caso 3 (Correcto): Configurar Servicio de Sala con Catering
    print("\n[Operación 3/10] Creación de Servicio Sala de Reuniones")
    srv_sala = SalaReuniones("SR-01", "Sala Executive VIP", tarifa_base=50000.0, horas_uso=4, incluye_catering=True)
    print(f"  ✅ Creado: {srv_sala} | Costo Calculado: ${srv_sala.calcular_costo_total():,.2f}")

    # Caso 4 (Correcto): Emitir Reserva 1
    print("\n[Operación 4/10] Emisión de Reserva 1 (Sala Executive)")
    gestor.procesar_reserva("RES-101", cli1, srv_sala)

    # Caso 5 (Error Controlado): Intentar Crear Sala con Horas Cero/Negativas
    print("\n[Operación 5/10] Creación de Servicio Sala con Horas Inválidas")
    try:
        srv_err = SalaReuniones("SR-02", "Sala Express", tarifa_base=30000.0, horas_uso=0)
    except ValidacionServicioError as err:
        logging.error(f"Fallo en parametrización de servicio SR-02: {err}")
        print(f"  ❌ Excepción Capturada: {err}")

    # Caso 6 (Correcto): Registrar Cliente 2
    print("\n[Operación 6/10] Alta de Cliente 2 Válido")
    cli2 = gestor.alta_cliente("1012345678", "Laura Sofía Torres", "laura.torres@unad.edu.co")

    # Caso 7 (Correcto): Configurar Servicio Alquiler de Equipo
    print("\n[Operación 7/10] Creación de Servicio Alquiler de Servidor")
    srv_equipo = EquipoTecnologico("EQ-88", "Servidor Rack 32GB RAM", tarifa_base=75000.0, dias_alquiler=5)
    print(f"  ✅ Creado: {srv_equipo} | Costo Calculado: ${srv_equipo.calcular_costo_total():,.2f}")

    # Caso 8 (Correcto): Emitir Reserva 2
    print("\n[Operación 8/10] Emisión de Reserva 2 (Servidor)")
    gestor.procesar_reserva("RES-102", cli2, srv_equipo)

    # Caso 9 (Correcto): Configurar Asesoría Técnica Remota (Con Descuento)
    print("\n[Operación 9/10] Creación de Asesoría Especializada Remota")
    srv_asesoria = ConsultoriaEspecializada("AS-50", "Consultoría en Ciberseguridad", tarifa_base=90000.0, sesiones=3, es_remota=True)
    print(f"  ✅ Creado: {srv_asesoria} | Costo Calculado (Desc. 10% aplicado): ${srv_asesoria.calcular_costo_total():,.2f}")

    # Caso 10 (Error Controlado): Intentar Reserva con Cliente Nulo
    print("\n[Operación 10/10] Emisión de Reserva con Cliente Fallido/Nulo")
    gestor.procesar_reserva("RES-103", cli_bad, srv_asesoria)

    print("\n" + "=" * 80)
    print("    SIMULACIÓN CONCLUIDA EXITOSAMENTE SIN INTERRUPCIÓN DEL PROGRAMA    ")
    print("    Los registros de auditoría se guardaron en 'sistema_manjarres.log'    ")
    print("=" * 80)

if __name__ == "__main__":
    ejecutar_pruebas_sistema()