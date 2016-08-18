#!/usr/bin/env python

import argparse
import os
import sys

import fnmatch

from os.path import join, isfile
from shutil import copytree

def copyext_keeptree(src_dir, dest_dir, extensions, verbose):

    ext_standard = []
    for ext in extensions:
        if ext[0] != '.':
            ext = '.' + ext
        ext_standard.append(ext)
    ext_standard = tuple(ext_standard)

    ignore_func = lambda d, files: [f for f in files if isfile(join(d, f)) and not f.endswith(ext_standard)]
    copytree(src_dir, dest_dir, ignore=ignore_func)

## Return the list of files in the designated directory with extension provided by the user
# @param dir Input directory
# @param ext Extension of the files
def get_filelist_ext(dir, ext):
    filelist = []
    for file in os.listdir(dir):
        if file.endswith(ext):
            filelist.append(file)
    return filelist

## Checks extension at the end of the name provided
# @param name Name to check
# @param ext Extension to check (could be with or without '.', i.e. '.txt' or just 'txt' - it will add '.' automatically)
def check_extend(name, ext):
    if name == None or name == '' or ext == None or ext == '':
        return name

    if ext[0] != '.':
        ext = '.' + ext
    if name[-len(ext):] != ext:
        name += ext

    return name

## Tests functionality
def main(argv):
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "dir",
        help="Input directory"
    )
    parser.add_argument(
        "ext",
        help="Extension of files to filter"
    )

    args = parser.parse_args()

    print get_filelist_ext(args.dir, args.ext)


## Returns path,name,extension tuple from name
# @param name Name you want to split
# @param keepslash Keep slash at the end of the path or not
def fileparts(name, keepslash=True):
    e = os.path.splitext(name)[1][1:]
    n = os.path.basename(os.path.splitext(name)[0])
    p = os.path.dirname(name)

    if p=='':
        p = '.'

    if keepslash:
        p = p + '/'

    return (p,n,e)



def find_files_ext(dir, extensions):

    ext_standard = []
    for ext in extensions:
        if ext[0] != '.':
            ext = '.' + ext
        ext_standard.append(ext)

    matches = []
    for root, dirs, files in os.walk(dir):
        for filename in files:
            if filename.endswith(ext_standard):
                matches.append(filename)

    return matches

if __name__ == '__main__':
    main(sys.argv)


