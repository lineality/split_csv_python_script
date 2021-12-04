# split_csv_python_script

Python script to make split .csv files into 
an even number of split files (2, 4, 6, etc.)
that collectively contain all of the data.

For example, if one file is too big, and you want to make
four smaller files that contain all the data.

This requires pandas to be installed (e.g. in pipenv shell).

If you want the file split into 4 files,
set the split number to 2. 

This will automatically split all files in the directory
the specified number of times.

For example:
Running this script two times, each time set to: 2 (resulting files)
is the same as running this script one time, set to 4 (resulting files).

The original file is retained, but the name as 
```
_original
```
added to the end. E.g.
``
MY_FILE.csv_original
```
