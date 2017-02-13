#! /usr/bin/python3
# -*- coding: utf-8 -*-

import datetime
import os
import settings
import shutil
from collections import defaultdict


def debug_print(text):
    """Print text if debugging mode is on"""
    if settings.debug:
        print(text)


def organize(files):
    files_by_extensions = defaultdict(list)
    for file in files:
        filename, file_extension = os.path.splitext(file)
        files_by_extensions[file_extension].append(file)

    files_by_type = defaultdict(list)
    for extension in files_by_extensions:
        for folder in settings.extensions:
            if extension in settings.extensions[folder]:
                files_by_type[folder] += files_by_extensions[extension]

    for (folder, files) in files_by_type.items(): 
        organized_folder = settings.folder + folder
        if not os.path.exists(organized_folder):
            os.makedirs(organized_folder)
        for file in files:
            new_path = organized_folder + '\\' + file
            debug_print('File ' + file + ' moved')
            shutil.move(settings.folder + file, new_path)


def main():
    debug_print('Task started at: ' + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    files = [f for f in os.listdir(settings.folder) if os.path.isfile(os.path.join(settings.folder, f))]
    print(files)
    if not files:
        debug_print('No files to organize in folder')
    else:
        organize(files)
    debug_print('Task is done')

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit(1)
