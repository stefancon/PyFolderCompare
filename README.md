# PyFolderCompare
Quick and dirty folder comparison tool for finding either duplicate or missing files (and optionally copy search hits)

## Example:
```
python3 .\folder_compare.py --folder "a" --compare "b" --dst "C:\Users\Example\Desktop\c" --recursive --dismiss_subfolders -mode duplicates
```

## Parameters:
``-folder``: Folder containing files to compare.
``-compare``: Folder containing comparison files.
``-dst``: Destionation path to copy search hit files (optional).
``-dismiss-subfolders``: When choosing a destionation path copy all search hits to parent folder (also from search hits inside subfolders).
``-no-dismiss-subfolders``: When choosing a destionation path copy all search hits and keep folder structure (from ``-folder``).
``-mode``: ``duplicates`` (default) or ``missing``.
``-recursive``: Also traverse subfolders.
``-no-recursive``: Ignore subfolders.
