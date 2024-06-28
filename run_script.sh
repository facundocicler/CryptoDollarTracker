#!/bin/bash

# Activa el entorno virtual
source /home/ubuntu/CryptoUSD/myenv/bin/activate

# Cambia al directorio del proyecto
cd /home/ubuntu/CryptoUSD/src

# Establece el PYTHONPATH para incluir el directorio raíz del proyecto
export PYTHONPATH=/home/ubuntu/CryptoUSD

python main.py