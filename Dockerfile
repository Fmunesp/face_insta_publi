# Imagen base de Python 3.9
FROM python:3.9-slim

# Establecer el directorio de trabajo dentro del contenedor docker
WORKDIR /app

# Copiar los archivos de requirements (si existen)
COPY app/requirements.txt ./

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt || echo "No requirements.txt found"

# Copiar el resto de los archivos del proyecto
COPY app/ .

# Comando por defecto al iniciar el contenedor
CMD ["python3"]