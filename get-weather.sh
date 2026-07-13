#!/bin/bash
# get-weather.sh - ejecuta main.py con el entorno conda correcto

source /home/micaela/miniforge3/etc/profile.d/conda.sh
conda activate base

cd /home/micaela/Proyecto_FinalG3
python3 main.py
