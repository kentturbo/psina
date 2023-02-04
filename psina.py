import os
import yaml

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

with open("folder_paths.yml", 'r') as stream:
    try:
        folder_paths = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)

FOLDERS = [folder_paths["folder_webm"], folder_paths["folder_pic"], folder_paths["folder_txt"], folder_paths["folder_other"]]

def observe():
    observer = Observer()
    observer.start()
    
def achoice():
    while True:
        userinput = input(f'где будем шалить? '
                         '1. текущая директория, '
                         '2. загрузки, '
                         '3. загрузки в домашней директории, '
                         '4. выход '
                         'ваш выбор: ')

        try:
            number = int(userinput)
        except ValueError:
            print('ты че вообще ввел, ебланище?')
            continue

        if number == 1:
            print('слушаюсь и повинуюсь, мой господин.')
            folder_track = os.getcwd()
        elif number == 2:
            print('ну ладно.')
            folder_track = '/home/files/documents/загрузки'
        elif number == 3:
            print('хорошо, мой господин.')
            folder_track = '~/Downloads'
        elif number == 4:
            print('ну и пошел нахуй, выблядок обоссанный. я бы об твое еблище окурки тушил')
            quit()
        else:
            print('ты че вообще ввел, ебланище?')
            continue

        break

for folder in FOLDERS:
    if not os.path.exists(folder):
        os.mkdir(folder)

achoice()
observe()

while True:
    for filename in os.listdir(folder_paths["folder_track"]):
        if filename.endswith(".MHT") or filename.endswith(".part"):
            continue
        
        extension = filename.rsplit('.', 1)
        if len(extension) == 1:
            continue

        ext = extension[-1].lower()
        file = os.path.join(folder_paths["folder_track"], filename)

        if ext in ['webm', 'mp4', 'mov']:
            new_path = os.path.join(folder_paths["folder_webm"], filename)
        elif ext in ['jpg', 'png', 'gif', 'webp', 'jpeg', 'jfif']:
            new_path = os.path.join(folder_paths["folder_pic"], filename)
        elif ext in ['txt', 'pdf', 'doc', 'docx', 'xlsx']:
            new_path = os.path.join(folder_paths["folder_txt"], filename)
        else:
            new_path = os.path.join(folder_paths["folder_other"], filename)

        os.rename(file, new_path)

