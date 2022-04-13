import os
import shutil
from argparse import ArgumentParser
from enum import Enum

class Mode(Enum):
    duplicates = 'duplicates'
    missing = 'missing'

    def __str__(self):
        return self.value

parser = ArgumentParser()
parser.add_argument("-folder", "--folder", dest="folder",
                    help="find single files in this folder")
parser.add_argument("-compare", "--compare", dest="compare",
                    help="compare to this folder")
parser.add_argument("-dst", "--dst", dest="dst",
                    help="destination folder for single files")
parser.add_argument('-mode', '--mode', type=Mode, choices=list(Mode), default=Mode.duplicates,
                    help="duplicates or missing")
parser.add_argument("-recursive", "--recursive", dest="recursive",
                    action='store_true', help="include subfolders")
parser.add_argument("-no-recursive", "--no-recursive", dest="recursive",
                    action='store_false', help="include subfolders")
parser.add_argument("-dismiss_subfolders", "--dismiss_subfolders", dest="dismiss_subfolders",
                    action='store_true', help="dismiss subfolders when copying singles")
parser.add_argument("-no-dismiss_subfolders", "--no-dismiss_subfolders", dest="dismiss_subfolders",
                    action='store_false', help="dismiss subfolders when copying singles")

args = parser.parse_args()

def traverse_folder(folderpath):
    _files = []
    _fullpaths = []
    if args.recursive:
        for root, dirs, files in os.walk(folderpath, topdown=True):
            path = root.split(os.sep)
            for file in files:
                _files.append(file)
                _fullpaths.append(os.path.join(root, file))
    else:
        for file in os.listdir(folderpath):
            if os.path.isfile(os.path.join(folderpath, file)):
                _files.append(file)
                _fullpaths.append(os.path.join(folderpath, file))
    return _files, _fullpaths

def consume_hit(path, file):
    if args.dst:
        if args.dismiss_subfolders:
            os.makedirs(args.dst, exist_ok=True)
            shutil.copyfile(path, os.path.join(args.dst, file))
        else:
            rel_path = os.path.relpath(path, args.folder)
            dst_path = os.path.join(args.dst, rel_path)
            os.makedirs(os.path.dirname(dst_path), exist_ok=True)
            shutil.copyfile(path, dst_path)

def main():
    files, files_paths = traverse_folder(args.folder)
    if len(files) == 0:
        print("No files found to compare.")
        exit()
    comparison, comparison_paths = traverse_folder(args.compare)
    if len(comparison) == 0:
        print("No comparison files found.")
        exit()

    hits = 0
    for idx, i in enumerate(files):
        if args.mode == Mode.duplicates and i in comparison:
            print(files_paths[idx])
            hits += 1
            if args.dst:
                consume_hit(files_paths[idx], files[idx])
        elif args.mode == Mode.missing and i not in comparison:
            print(files_paths[idx])
            hits += 1
            if args.dst:
                consume_hit(files_paths[idx], files[idx])

    print("{length} single files in total.".format(length=hits))
    if args.mode == Mode.missing and args.dst: print("Copied single files to {dst}".format(dst=args.dst))
    if args.mode == Mode.duplicates and args.dst: print("Copied duplicate files to {dst}".format(dst=args.dst))
    args.dismiss_subfolders: print("Dismissed subfolders in new destination.")

if __name__ == "__main__":
    main()
