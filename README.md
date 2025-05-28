# Proyecto_final
1. Contexto

Una comunidad desea gestionar de forma organizada el registro de actividades físicas, 
recreativas y de salud de sus miembros (spinning, fisioterapia, rumba y fortalecimiento). 
Se requiere una aplicación que permita registrar los datos de los usuarios, gestionar su 
asistencia, calcular pagos, generar estadísticas y almacenar esta información para su 
posterior análisis. Todo esto deberá hacerse a través de una interfaz gráfica sencilla, 
organizada con programación orientada a objetos, y el proyecto debe ser subido con 
control de versiones a GitHub. El trabajo se realiza en grupos de máximo 3 personas.


2. Requerimientos técnicos
Módulos obligatorios a utilizar:
- tkinter: para la interfaz gráfica de registro.
- pandas: para la manipulación de datos registrados.
- matplotlib: para generar gráficos.
- POO: todo el código debe estar organizado en clases.
- GitHub: subir el proyecto completo con control de versiones.


3. Descripción del Proyecto

3.1 Interfaz Gráfica Inicial (Tkinter)

Debe permitir:
- Registro de nombre, edad, actividad, meses y decir el valor pagado a partir de la 
cantidad de clases que pago ese mes, teniendo en cuenta que por clase se paga:
Spinning = 7000
Fisioterapia = 10000
Rumba = 5000
Fortalecimiento = 6500
- Botones para: registrar nuevo usuario, modificar usuario, eliminar usuario, mostrar 
todos los registros, y generar reportes.

3.2 Lógica Interna (POO)

Se deben implementar al menos dos clases principales: Usuario Y Análisis.

3.3 Análisis y Visualización (Pandas + Matplotlib)

Debe incluir un reporte con:
- Total de usuarios registrados.
- Identificación de usuarios con datos incompletos o nulos (La idea es que el botón de 
modificar me permita añadir también esos datos vacíos).
- Promedio de pagos.
-Actividad con mayor número de inscritos.
- Usuario que más ha pagado.
Visualizaciones sugeridas:
- Gráfico de barras de usuarios por actividad.
- Histograma de edades.
- Gráfico circular de inscripciones por actividad.
