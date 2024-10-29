# CryptoDollarTracker
## Descripción 

CryptoDollarTracker es una aplicación de Python diseñada para obtener datos en tiempo real sobre la cotización del dólar y las criptomonedas. Utiliza APIs para obtener estos datos y los procesa para generar informes o alertas. Este proyecto está configurado para ejecutarse en una instancia EC2 de AWS.

## Características 

   * Obtención de datos en tiempo real sobre la cotización del dólar.
   * Obtención de datos en tiempo real sobre varias criptomonedas.
   * Integración con Amazon SNS para enviar notificaciones.
   * Configuración sencilla y automatizada mediante scripts de shell.

## Requisitos 

   * Python 3.8+
   * Una instancia EC2 de AWS
   * Claves de API para los servicios utilizados (por ejemplo, CryptoCompare)
    
## Instalación 
### 1. Clonar el repositorio
Clona este repositorio en tu máquina local o en tu instancia EC2:
```bash
git clone https://github.com/facundocicler/CryptoDollarTracker.git
```
```bash
cd CryptoDollarTracker
```

### 2. Subir los archivos a la instancia EC2
Usa scp para transferir los archivos a la instancia EC2:
```bash
scp -i "mi_instancia.pem" -r CryptoDollarTracker/ username@your-ec2-instance.amazonaws.com:~
```

### 3. Conectarse a la instancia EC2
Conéctate a tu instancia EC2:
```bash
ssh -i "mi_instancia.pem" username@your-ec2-instance.amazonaws.com
```
```bash
cd CryptoDollarTracker
```

### 4. Ejecutar el script de configuración
Ejecuta el script de configuración setup.sh para crear el entorno virtual e instalar las dependencias:
```bash
chmod +x setup.sh
```
```bash
./setup.sh
```

### 5. Ejecutar el script principal
Ejecuta el script run_script.sh para iniciar la aplicación:
```bash
chmod +x run_script.sh
```
```bash
./run_script.sh
```

## Uso 
El script main.py en el directorio src es el punto de entrada principal de la aplicación. Puedes modificarlo según tus necesidades para ajustar la lógica de obtención de datos o las notificaciones.

## Estructura del Proyecto 

    CryptoDollarTracker/
    │
    ├── myenv/                # Entorno virtual
    ├── requirements.txt      # Dependencias del proyecto
    ├── setup.sh              # Script de configuración
    ├── run_script.sh         # Script para ejecutar la aplicación
    ├── src/                  # Código fuente del proyecto
    │   ├── main.py           # Script principal
    │   ├── data_fetchers.py  # Módulo para obtener datos
    │   ├── sns_client.py     # Cliente para Amazon SNS
    │   └── utils.py          # Funciones utilitarias
    └── README.md             # Este archivo
