import os
import shutil
from pathlib import Path


path = Path.home() / 'Desktop'    # desktop path
pdf_folder = Path.home() / 'Desktop' / 'pdf files'
print(path)

pdf_folder.mkdir(exist_ok=True)

for item in os.listdir(path):
    item_full_path = os.path.join(path, item)
    filename, file_extension = os.path.splitext(item_full_path) # extracting both filename and file extension

    if os.path.isfile(item_full_path) and file_extension == '.pdf': #checks first is it a file and then if its a pdf file
        shutil.move(item_full_path, pdf_folder) # if its a pdf it will move it into this folder
    else:   
        continue
