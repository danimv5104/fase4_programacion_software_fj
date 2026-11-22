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

### 📝 Descripción de la Solución
Este proyecto consiste en la implementación de una aplicación modular en Python diseñada bajo el paradigma de la **Programación Orientada a Objetos (POO)** para la empresa **Software FJ**. 

La aplicación gestiona clientes, servicios y reservas sin utilizar bases de datos externas, apoyándose en estructuras de datos en memoria, control riguroso de excepciones personalizadas y auditoría de operaciones mediante archivos de registro (`.log`).

---

### ⚙️ Principios de POO y Requerimientos Implementados

1. **Encapsulamiento (`ClienteSoftwareFJ`):**
   * Atributos privados (`_cedula`, `_nombre_completo`, `_email`) protegidos mediante decoradores `@property`.
   * Validaciones estrictas en los setters para evitar campos vacíos o correos con formato inválido.

2. **Abstracción y Herencia (`ServicioBase`):**
   * Clase base abstracta utilizando el módulo `abc`.
   * Subclases especializadas para las 3 líneas de negocio:
     * `SalaReuniones`: Incluye cobro por horas y adicionales de catering.
     * `EquipoTecnologico`: Incluye días de alquiler y seguro de protección.
     * `ConsultoriaEspecializada`: Incluye cálculo por sesiones y descuento por modalidad remota.

3. **Polimorfismo:**
   * Cada subclase sobrescribe de forma única el método abstracto `calcular_costo_total()`.

4. **Manejo de Excepciones Personalizadas:**
   * Jerarquía de clases derivadas de `Exception`: `ErrorBaseSoftwareFJ`, `ValidacionClienteError`, `ValidacionServicioError` y `GestionReservaError`.
   * Estructuración de operaciones con bloques `try / except / else / finally`.

5. **Auditoría y Logs (`sistema_manjarres.log`):**
   * Registro automático de eventos de éxito (`logging.info`) y fallos (`logging.error`) con marcas de tiempo.

6. **Demostración de Estabilidad:**
   * Simulación de 10 operaciones consecutivas (combinando datos válidos e inválidos) demostrando la tolerancia a fallos del sistema sin caídas del programa.

---

### 📁 Estructura del Repositorio
* `ANEXO_3_FASE_4_Manjarres.py`: Código fuente principal de la solución.
* `sistema_manjarres.log`: Archivo generado automáticamente con el historial de eventos e incidencias.
* `README.md`: Documentación técnica del proyecto.

---

### 🚀 Instrucciones de Ejecución
Para ejecutar el script en cualquier entorno con Python 3:

```bash
python ANEXO_3_FASE_4_Manjarres.py