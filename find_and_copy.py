##find_and_copy.py

##a function to look through a directory of files, find a file
##of a certain type, and if it exists, copy it to a new
#common location

##by Ryan Neely 12/3/19

import os
import shutil

def find_and_copy(f_source,f_dest,ext=None,name=None,verbose=False):
    """
    This function looks in one folder for a file with certain 
    characteristics, and copies it to another folder. 
    Args:
        -f_source: source folder to look in
        -f_dest: destination folder to copy file to
        -ext: optional extension of target file 
            **note that this will first filter by extension, and then by name***
        -name: optional name of target file, without extension
        -verbose: if True, displays messages
    """
    ##get all of the files in the source folder
    target_files = os.listdir(f_source)
    ##find any files that meet the given criteria
    if ext is not None: ##first filtering by extension
        target_files = [x for x in target_files if x.endswith(ext)]
    if name is not None:
        target_files = [x for x in target_files if os.path.splitext(x) == name]
    if len(target_files) > 0:
        for f in target_files:
            f_full = os.path.join(f_source,f)
            shutil.copy(f_full,f_dest)
            ##NOTE: not sure why this doesn't throw a shutil.SameFileError 
            # when the file exists already in the destination
    else:
        if verbose:
            print("No files matching input criteria found")

