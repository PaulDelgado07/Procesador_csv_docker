FROM python:3.11.11-slim-bookworm

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Rutas configurables para entrada y salida
ENV INPUT_PATH=/app/datos/ventas.csv \
    OUTPUT_DIR=/app/salida

RUN groupadd --system appgroup && \
    useradd --system --gid appgroup --create-home appuser


COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY procesar.py .

USER appuser

CMD ["python", "procesar.py"]
