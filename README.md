# PyFolderCompare
Quick and dirty folder comparison tool for finding either duplicate or missing files (and optionally copy search hits to another location). Currently comparison only based on filenames.

## Arguments:
- ``-folder``: Folder containing files to compare.
- ``-compare``: Folder containing files to compare to.
- ``-mode``: ``duplicates`` (default) or ``missing``.
- ``-dst``: Destination path to copy search hits i. e. duplicate or missing files (optional).
- ``-dismiss-subfolders``/``-no-dismiss-subfolders`` (default): When selecting a destination directory for copying the search hits, copy all files directly here. Otherwise, the folder structure of the search hits will be recreated when copying.
- ``-recursive`` (default)/``-no-recursive``: Also traverse subfolders when searching for duplicate or missing files.

## Example:
Find all files that exist in ``a`` and ``b``. Therefore traverse subfolders in ``a`` and ``b``. Copy found duplicates to ``dst`` (without recreating subfolders from ``a`` and ``b``).
```
python3 .\folder_compare.py -folder "a" -compare "b" -mode duplicates -dst "C:\Users\Example\Desktop\c" -dismiss_subfolders -recursive
```
