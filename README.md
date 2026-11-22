# Fase 4 - Componente Práctico: Prácticas Simuladas
## Sistema Integral de Gestión de Servicios y Reservas "Software FJ"

### 📋 Información del Proyecto
* **Estudiante:** Daniela Manjarres
* **Grupo Colaborativo:** 213023_153
* **Curso:** Programación (213023)
* **Programa:** Ingeniería de Sistemas
* **Institución:** Universidad Nacional Abierta y a Distancia (UNAD)
* **Escuela:** Escuela de Ciencias Básicas, Tecnología e Ingeniería (ECBTI)
* **Fecha:** Noviembre 2026

---

### 📝 Descripción General
Aplicación modular desarrollada en Python bajo el paradigma de la **Programación Orientada a Objetos (POO)** para la empresa **Software FJ**. El sistema gestiona clientes, servicios tecnológicos y reservas en memoria (sin bases de datos externas), garantizando la estabilidad operativa mediante control riguroso de excepciones personalizadas y auditoría continua de eventos.

---

### ⚙️ Arquitectura y Principios de POO Implementados

1. **Encapsulamiento (`ClienteSoftwareFJ`):**
   * Atributos privados (`_cedula`, `_nombre_completo`, `_email`) protegidos mediante decoradores `@property`.
   * Setters con validaciones estrictas para impedir registros vacíos o correos sin sintaxis válida (`@` y `.`).

2. **Abstracción y Herencia (`ServicioBase`):**
   * Clase base abstracta utilizando el módulo `abc` (`ABC` y `@abstractmethod`).
   * Subclases derivadas especializadas para 3 líneas de negocio:
     * `SalaReuniones`: Cálculo por horas de uso más adicionado opcional por catering.
     * `EquipoTecnologico`: Tarifas por días de alquiler e inclusión de seguro de protección.
     * `ConsultoriaEspecializada`: Cobro por sesiones con descuento automático por modalidad remota.

3. **Polimorfismo:**
   * Sobrescritura del método abstracto `calcular_costo_total()` en cada subclase con reglas de negocio diferenciadas.

4. **Gestión en Memoria y Agregación (`ControladorSoftwareFJ`):**
   * Administración de objetos mediante colecciones internas (`list`), cumpliendo la restricción de cero motores de bases de datos.

5. **Jerarquía de Excepciones Personalizadas:**
   * Estructura de errores derivados de `Exception`: `ErrorBaseSoftwareFJ`, `ValidacionClienteError`, `ValidacionServicioError` y `GestionReservaError`.

6. **Manejo de Errores y Tolerancia a Fallos (`try / except / else / finally`):**
   * Bloques de control que capturan anomalías en runtime evitando cierres o caídas del sistema.

7. **Auditoría y Módulo de Logs (`sistema_manjarres.log`):**
   * Registro automatizado con la librería `logging` de eventos exitosos (`logging.info`) y excepciones (`logging.error`) con estampas de tiempo (`asctime`).

8. **Simulación de Estabilidad (10 Operaciones):**
   * Demostración con escenarios válidos e inválidos para comprobar el comportamiento del software en producción.

---

### 📁 Estructura del Repositorio
* `ANEXO_3_FASE_4_Daniela_Manjarres.py`: Código fuente principal en Python.
* `sistema_manjarres.log`: Archivo de auditoría generado automáticamente.
* `README.md`: Documentación técnica del proyecto.
* `Anexo 3 - Problema a desarrollar Fase 4.pdf`: Guía de requerimientos.

---

### 🚀 Instrucciones de Ejecución
Para ejecutar la simulación desde la terminal:

```bash
python ANEXO_3_FASE_4_Daniela_Manjarres.py