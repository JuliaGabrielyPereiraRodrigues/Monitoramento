import os
import sys
import time
import logging
import django
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(BASE_DIR)

# Definir configurações do Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Monitor.settings')
django.setup()  

from App.models import File  

class MyHandler(FileSystemEventHandler):
    def __init__(self, target_files):
        self.target_files = target_files

    def on_modified(self, event):
        if not event.is_directory:
            file_name = os.path.basename(event.src_path)
            if event.src_path in self.target_files:
                try:
                    File.objects.update_or_create(
                        name=file_name, defaults={'path': event.src_path}
                    )
                    logging.info(f"Arquivo atualizado/criado: {file_name}")
                except Exception as e:
                    logging.error(f"Erro ao atualizar/criar arquivo: {e}")

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

    # Caminho absoluto para a pasta "teste"
    path = os.path.join(BASE_DIR, 'teste')
    
    if not os.path.exists(path):
        logging.error(f"O diretório {path} não existe!")
        sys.exit(1)

        target_files = ['teste.txt']


    event_handler = MyHandler(target_files)
    observer = Observer()
    observer.schedule(event_handler, path, recursive=False)
    observer.start()
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
