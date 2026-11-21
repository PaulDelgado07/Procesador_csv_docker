
# Procesador de Datos CSV con Docker

## Descripción

Este proyecto permite procesar archivos CSV de ventas utilizando Python y pandas dentro de un contenedor Docker.

El programa limpia los datos, calcula el total de las ventas y genera un resumen de ingresos por producto.

El objetivo es demostrar la portabilidad de una aplicación mediante Docker, utilizando buenas prácticas de construcción de imágenes.

## Tecnologías utilizadas

- Python 3.11
- pandas 2.2.3
- Docker
- Git y GitHub

## Estructura del proyecto

```text
procesador-csv-docker/
├── procesar.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── .gitignore
├── README.md
├── datos_ejemplo/
│   └── ventas.csv
└── evidencias/
```

## Requisitos

- Docker instalado y funcionando.
- No es necesario instalar Python localmente.

## Construcción de la imagen

Desde la carpeta principal del proyecto:

```bash
docker build -t procesador-csv:1.0.0 .
```

## Ejecución del contenedor

Crear la carpeta de salida:

```bash
mkdir -p salida
```

Ejecutar:

```bash
docker run --rm \
  -e INPUT_PATH=/app/datos/ventas.csv \
  -e OUTPUT_DIR=/app/salida \
  -v "$(pwd)/datos_ejemplo:/app/datos:ro" \
  -v "$(pwd)/salida:/app/salida" \
  procesador-csv:1.0.0
```

El programa lee el CSV desde un volumen de entrada y guarda los resultados en un volumen de salida.

## Variables de entorno

| Variable | Descripción | Valor predeterminado |
|---|---|---|
| INPUT_PATH | Ruta del archivo CSV de entrada | /app/datos/ventas.csv |
| OUTPUT_DIR | Directorio donde se guardan los resultados | /app/salida |

Las variables pueden modificarse sin cambiar el código fuente.

## Volúmenes

| Carpeta local | Ruta del contenedor | Función |
|---|---|---|
| datos_ejemplo | /app/datos | Entrada, solo lectura |
| salida | /app/salida | Archivos generados |

## Resultados esperados

Al ejecutar el contenedor:

```text
Procesamiento completado correctamente.
Registros procesados: 6
Ingreso total: $3190.00
Archivos generados en: /app/salida
```

Se generan dos archivos:

- ventas_limpias.csv
- resumen.csv

Ejemplo de resumen.csv:

```csv
producto,unidades_vendidas,ingreso_total
Laptop,3,2550
Monitor,2,400
Mouse,9,135
Teclado,3,105
```

## Buenas prácticas implementadas

- Imagen base Python slim con versión fija.
- Instalación de dependencias antes de copiar el código para aprovechar la caché de Docker.
- Ejecución con usuario sin privilegios.
- CMD en formato exec.
- Variables de entorno para configurar rutas.
- Volúmenes para separar los datos del contenedor.
- Archivo .dockerignore para excluir archivos innecesarios.
- Dependencias con versiones fijas.

## Puertos

No se necesita exponer ningún puerto porque la aplicación procesa archivos CSV y no ejecuta un servidor web.

## Publicación en Docker Hub

La imagen se publicará con la etiqueta 1.0.0.

Enlace de Docker Hub: pendiente de publicación.

## Evidencias

Las capturas de construcción, ejecución y publicación se encuentran en la carpeta evidencias.

## Autor

Proyecto académico de Infraestructura y Servicios Cloud para Procesamiento de Datos.

Universidad de Guayaquil.
