# -*- coding: utf-8 -*-
import os
import sys
from progress_bar import print_progress_bar
from time import sleep


def search_path(path=os.path.abspath(__file__)):
    '''
    функция определяет путь к файлу со скриптом
    '''
    return os.path.dirname(path)


def renamer(path, files):
    '''
    функция изменяет имя файла (скрипт для изображений)
    на имя папки содержащие изображения.
    p.s. для теста скрипта использовались файлы с расширением '.txt' 
    '''
    arg = []
    for f in files:
        if os.path.isfile(os.path.join(path, f)):
            if os.path.splitext(f)[-1] == '.txt':
                arg.append(os.path.join(path, f))
    dir_name, dir_name = os.path.split(path)
    new_name = dir_name
    padding = 4
    l = len(arg)
    print_progress_bar(0, l, prefix=('Progress rename folder: ' + path), suffix='Complite', lenght=50)
    for i, f in enumerate(arg):
        d = os.path.dirname(f)
        name, ext = os.path.splitext(os.path.basename(f))
        file_name = new_name + '_' + str(i+1).zfill(padding) + ext
        full_path = os.path.join(d, file_name)
        os.rename(f, full_path)
        sleep(0.1)
        print_progress_bar(i+1, l, prefix=('Progress rename folder: ' + path), suffix='complite', lenght=50)


def rename_folder(path):
    '''
    функция ищет все папки и файлы в дериктории со скриптом
    и запускает функцию переименования файлов
    '''
    list_dir = os.listdir(path)
    dirs = []
    files = []
    for d in list_dir:
        if os.path.isdir(os.path.join(path, d)):
            dirs.append(os.path.join(path, d))
        elif os.path.isfile(os.path.join(path, d)):
            files.append(os.path.join(path, d))
        else:
            print '?!'
    
    if files != []:
        renamer(path, files)

    if dirs != []:
        for d in dirs:
            rename_folder(d)

if __name__ == '__main__':
    rename_folder(search_path())
    raw_input()
