import os
import zipfile
import patoolib

folder_path = "/home/yhs/Downloads/misc3"

for file_name in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file_name)

    if file_name.endswith('.zip'):
        with zipfile.ZipFile(file_path, 'r') as zip_ref:
            zip_ref.extractall(folder_path)

        os.remove(file_path)

    elif file_name.endswith('.rar'):
        patoolib.extract_archive(file_path, outdir=folder_path)

        os.remove(file_path)
