#!/bin/bash

# Actualiza e instala los paquetes del sistema
sudo apt-get update -y

sudo apt-get install -y python3-pip python3-venv

# Crea el entorno virtual
python3 -m venv myenv

# Activa el entorno virtual
source myenv/bin/activate

# Instala las dependencias
pip install -r requirements.txt

echo "El entorno virtual se ha creado y las dependencias se han instalado exitosamente."
