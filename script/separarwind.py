import os
import shutil
from sklearn.model_selection import train_test_split
import glob

dir_origen = "..\\archive\\PotatoPlants"
dir_destino = "dataset"

if not os.path.exists(dir_destino):
    os.mkdir(dir_destino)
dir_destino = os.path.join(dir_destino, "data")
if not os.path.exists(dir_destino):
    os.mkdir(dir_destino)
sub_dirs = os.listdir(dir_origen)
for sub_dir in sub_dirs:
    sub_dir_path = os.path.join(dir_destino, sub_dir)
    if not os.path.exists(sub_dir_path):
        os.mkdir(sub_dir_path)
    imagenes = glob.glob(os.path.join(dir_origen, sub_dir, "*.JPG"))
    print(len(imagenes))
    _, porcentaje_imagenes = train_test_split(imagenes, test_size=0.2, random_state=42)
    for ruta_imagenes in porcentaje_imagenes:
        print("Train: ", ruta_imagenes)
        nombre = os.path.basename(ruta_imagenes)
        shutil.copy(ruta_imagenes, os.path.join(sub_dir_path, nombre))