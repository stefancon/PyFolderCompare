# PyFolderCompare
Quick and dirty folder comparison tool for finding either duplicate or missing files (and optionally copy search hits to another destination). Currently comparison only based on filenames.

## Example:
Find all files that exist in ``a`` and ``b``. Therefore traverse subfolders in ``a`` and ``b``. Copy found duplicates to ``dst`` (without recreating subfolders from ``a`` and ``b``).
```
python3 .\folder_compare.py --folder "a" --compare "b" --dst "C:\Users\Example\Desktop\c" --recursive --dismiss_subfolders --mode duplicates
```

## Parameters:
- ``-folder``: Folder containing files to compare.
- ``-compare``: Folder containing comparison files to compare to.
- ``-dst``: Destination path to copy search hit files (optional).
- ``-dismiss-subfolders``: When choosing a destionation path copy all search hits to parent folder (also from search hits inside subfolders).
- ``-no-dismiss-subfolders``: When choosing a destionation path copy all search hits and keep folder structure (from ``-folder``) (default).
- ``-mode``: ``duplicates`` (default) or ``missing``.
- ``-recursive``: Also traverse subfolders.
- ``-no-recursive``: Ignore subfolders (default).
