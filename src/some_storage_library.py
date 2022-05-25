import os
from os.path import exists
import pathlib
import shutil


project_root = pathlib.Path(__file__).parent.parent.resolve() 
destination = os.path.join(project_root, 'data', 'destination')


class SomeStorageLibrary:

    def __init__(self) -> None:
        print('Instantiating storage library...')
        if not os.path.isdir(destination):
            os.mkdir(destination)


    def load_csv(self, filename: str) -> None:
        print(f'Loading the following file to storage medium: {filename}')
        infile = os.path.join(project_root, 'data', 'destination',filename)
        if False == exists(infile):
            shutil.move(filename, destination)
            print('Load completed!')
            return
        else:
            print("File already exists, do something about that then try again")