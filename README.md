# split_csv_python_script

Python script to make split .csv files into 2 files
that each retain half of the data.

For example, if one file is too big, and you want to make
two smaller files that contain all the data.

This requires pandas to be installed (e.g. in pipenv shell).

This will make half-sized reductions in all .csv files
that are in the same directory as the script.

If you want the file split into 4 files,
set the split number to 2. 
