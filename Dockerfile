# Imagen base ligera con versión fija
FROM python:3.11.11-slim-bookworm

# Evitar archivos .pyc y activar salida inmediata
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Directorio de trabajo
WORKDIR /app

# Crear usuario sin privilegios
RUN groupadd --system appgroup && \
    useradd --system --gid appgroup --create-home appuser

# Copiar primero las dependencias para aprovechar la caché
COPY requirements.txt .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código de la aplicación
COPY procesar.py .

# Ejecutar como usuario sin privilegios
USER appuser

# Comando de ejecución en formato exec
CMD ["python", "procesar.py"]
