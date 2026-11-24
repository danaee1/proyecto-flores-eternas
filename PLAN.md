# Desarrollo del Proyecto: Eternal Flowers

## Fase 1: Configuración del Entorno
- [ ] Instalar Python 3.9+
- [ ] Crear y activar entorno virtual: `python -m venv venv` y `venv\Scripts\activate`
- [ ] Instalar dependencias: `pip install flask flask-cors mysql-connector-python`
- [ ] Instalar Node.js para frontend (opcional)
- [ ] Verificar MySQL está corriendo localmente

## Fase 2: Estructura Backend (Flask)
- [ ] Crear `app.py` con la app Flask base
- [ ] Configurar conexión MySQL (host, user, password, database)
- [ ] Diseñar tablas SQL:
  - `users` (cliente, email, telefono)
  - `orders` (id, user_id, fecha, estado, total, created_at)
  - `flowers` (id, nombre, precio, descripcion, imagen_url)
  - `order_items` (order_id, flower_id, cantidad)
- [ ] Implementar rutas API principales:
  - `GET /` - servir la página HTML
  - `GET /api/flowers` - listar flores disponibles
  - `POST /api/orders` - crear nuevo pedido
  - `GET /api/orders/:id` - obtener pedido por ID

## Fase 3: Frontend (HTML/CSS/JS)
- [ ] Crear `templates/index.html` con:
  - Calendar de selección de fecha (usar Flatpickr o similar)
  - Grid de flores disponibles con imágenes y precios
  - Cuadro de texto para descripción personalizada
  - Enlaces de redes sociales (iconos clickables)
- [ ] Estylizar con CSS coherente con la identidad del emprendedor
- [ ] JS para:
  - Fetch de flores desde `/api/flowers`
  - Validación de formulario de pedido
  - Mostrar confirmación al submit

## Fase 4: Integración de Funciones Clave
- [ ] **Calendar**: Integrar selector de fecha en el formulario de pedido
- [ ] **Social media links**: Agregar hrefs a WhatsApp, Instagram, Facebook del emprendedor
- [ ] **Text input**: Manejo del campo de descripción de elementos en el pedido

## Fase 5: Base de Datos y Persistencia
- [ ] Crear migraciones SQL iniciales
- [ ] Insertar datos de prueba (al menos 5 tipos de flores)
- [ ] Probar creación de pedido completo (flower + items + fecha)

## Fase 6: Testing y Verificación
- [ ] Iniciar servidor: `python app.py`
- [ ] Abrir http://localhost:5000 en navegador
- [ ] Probar: agregar flores al carrito → seleccionar fecha → submit
- [ ] Verificar que los datos se guarden en MySQL

## Fase 7: Despliegue (futuro)
- [ ] Configurar variables de entorno (DB credentials)
- [ ] Considerar PostgreSQL o MySQL en la nube
- [ ] Deploy a hosting compatible con Flask/MySQL