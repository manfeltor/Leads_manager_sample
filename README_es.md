
## Descripción del Proyecto

### Nombre del Proyecto
*INTRALOG leads manager*

### Descripción
*Este Leads Manager es una herramienta CRM personalizada en desarrollo diseñada para optimizar la gestión de leads para un equipo de ventas. Incluye funciones como la asignación de leads, seguimiento de estado, métricas de gestión y análisis de campañas, todo integrado en una interfaz web fácil de usar.*

### Características Principales

- **Gestión de Leads:**
  - Extrae datos desde plugins personalizados de WP, visualiza y gestiona leads con información detallada realizando una primera clasificación.
  - Asigna leads a usuarios específicos y realiza un seguimiento del progreso.
 
- **Generación de Usuarios Personalizados:**
  - Crea y edita usuarios con roles específicos y campos relevantes.
  - Gestiona usuarios (para la administración), y edita tu propio perfil para una mejor personalización y seguridad.
  
- **Gestión de Roles de Usuario:**
  - Define roles de usuario como Admin, Gerente y Empleado.
  - Gestiona permisos de usuario según los roles.

- **Formularios de CRM Personalizados:**
  - Generación dinámica de formularios para diferentes tipos de leads.
  - Almacena y gestiona las presentaciones de formularios con registros detallados para el análisis de comportamiento.
 
- **Autenticación de Usuarios:**
  - Sistema de registro y login seguro.
  - Gestión de perfiles que incluye el cambio de contraseña y asignación de roles.

- **Panel de Análisis:**
  - Visualiza métricas clave e indicadores de rendimiento (en desarrollo).
  - Filtra datos por fecha, estado y usuario asignado.

- **Análisis de Campañas (en desarrollo):**
  - Asocia leads con campañas de marketing.
  - Realiza un seguimiento de la efectividad de cada campaña con paneles de análisis para la alta gerencia.
 
  Para ver más características planificadas, consulta la sección de estado.

### Tecnología Utilizada

- **Python**: El lenguaje de programación principal utilizado para el desarrollo backend.
- **Django**: El framework web utilizado para construir el backend y manejar la estructura MVC.
- **SQLite**: El sistema de base de datos utilizado para el desarrollo y pruebas (se reemplazará por PostgreSQL o MSQLS en producción, aún en evaluación).
- **HTML/CSS**: Para construir la estructura y el estilo del frontend.
  - **W3.CSS**: Un framework CSS utilizado para el diseño y la capacidad de respuesta.
  - **FontAwesome**: Biblioteca de iconos utilizada para mejorar la interfaz de usuario.
- **JavaScript**: Utilizado para agregar interactividad al frontend.
  - **Vanilla JS**: Para manipulación básica del DOM y manejo de eventos.
- **Git**: Sistema de control de versiones utilizado para gestionar el código y la colaboración.
- **GitHub**: Servicio de alojamiento para el control de versiones utilizando Git, donde se almacena el repositorio del proyecto.
- **Django REST Framework**: Para la construcción de APIs (si es aplicable).
- **Celery**: Cola de tareas utilizada para manejar tareas asincrónicas (en desarrollo).
- **Docker**: Herramienta de contenedorización utilizada para crear y gestionar contenedores (se implementará una vez que esté listo para la producción).
- **Gunicorn**: Servidor HTTP WSGI para ejecutar aplicaciones Django en producción (se implementará una vez que la contenedorización esté lista).

### Herramientas de Desarrollo

- **VS Code**: Editor de código preferido para el desarrollo.
- **SQLite Browser**: Para gestionar la base de datos SQLite durante el desarrollo.

### Implementación

- **en sitio**: Se implementará en un servidor local como herramienta interna del cliente.

### Estado
- **Estado Actual:** *INTRALOG CRM leads Manager está actualmente en desarrollo, a la espera de definiciones de la alta gerencia para las últimas funcionalidades.*
- **Características Planificadas:**
  - *Análisis de Campañas:* *Esta característica asociará la fuente de campañas de marketing con cada lead para estudiar la eficiencia de la configuración y combinaciones de cada campaña. Actualmente estamos recopilando los datos históricos relevantes de las campañas para planificar la lógica del análisis.*
  - *Rendimiento Comercial:* *La gerencia podrá realizar un seguimiento del rendimiento del equipo en su conjunto y de cada miembro con la funcionalidad de registro de eventos, que proporcionará análisis en tiempo real para aprovechar las áreas de mejora e identificar las mejores habilidades y prácticas para replicar en el resto del equipo.*
  - *Alertas en tiempo real:* *Esta función enviará alertas personalizadas por correo y WhatsApp sobre leads potenciales relevantes. La API y el proveedor de correo transaccional ya están configurados. Lo que falta es la retroalimentación del equipo comercial sobre qué eventos deberían activar los correos.*

### Hoja de Ruta

### En Progreso
- Actualmente finalizando los detalles del panel de control de estado general de leads.

### Próximos Pasos
- **Q3 2024:** Panel de control terminado con una visión general del estado general de los leads.
- **Q4 2024:** Definiciones de datos configuradas y configuración para métricas de gestión, alertas automatizadas por correo.
- **Q1 2025:** Algoritmos definidos y carga de datos para el análisis de campañas.
- **Q2 2025:** Pruebas y despliegue.

### Instalación

Sigue estos pasos para configurar el proyecto en tu máquina local.

### Requisitos Previos

Asegúrate de tener lo siguiente instalado en tu máquina:

- **Python 3.8+**
- **Django 4.0+**
- **SQLite** (u otra base de datos si estás utilizando una)
- **Git**

### Clonar el Repositorio

Primero, clona el repositorio en tu máquina local usando Git:

```bash
git clone https://github.com/manfeltor/Leads_manager_sample
cd Leads_manager_sample
```

### Configurar el Entorno Virtual (recomendado)

```bash
python -m venv env
source env/bin/activate
```

### Instalar Dependencias

```bash
pip install -r requirements.txt
```

### Aplicar Migraciones

Para configurar tu base de datos

```bash
python manage.py migrate
```

### Base de Datos de Ejemplo para Ejecución

- Asegúrate de que la base de datos incluida esté copiada en el directorio raíz del proyecto.

**Nota:** La base de datos de ejemplo contiene un subconjunto de datos anonimizados que simulan el entorno real. La base de datos original y las credenciales de la API son propietarias. Si necesitas una demostración o acceso adicional, por favor, contacta conmigo en manfeltor@live.com.

### Ejecutar el Servidor de Desarrollo

Inicia el servidor de desarrollo de Django en modo inseguro para servir archivos estáticos:

```bash
python manage.py runserver --insecure
```

### Contribuidores
- **Desarrollador Principal:** *Felipe Torres*

### Licencia
*Licencia GPL-3.0, [lee el documento completo](LICENSE).*
