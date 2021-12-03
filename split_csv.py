# -*- coding: utf-8 -*-

"""
2021.12.03
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
"""

import pandas as pd
import os
import glob





# flag
file_ok = False

# check to see if given file name works, if not ask again
while file_ok is False:

    try:
        # Ask how many files to split the file into?
        number_of_final_files = int( input("Files divided into how many pieces? (even number) \n ") )

        number_of_reductions = int( number_of_final_files / 2 )

        file_ok = True

    except:
        file_ok is False
        print("That did not work. Please try an even integer (like 2, 4, 6, etc.) \n")

def reduce_csv():

    # get list of csv files
    file_list = glob.glob("*.csv")

    # iterate through list of csv files
    for your_file_name in file_list:

        file_counter = 1

        # load csv into pandas
        df = pd.read_csv( your_file_name )

        #############
        # First Half
        #############
        # pick where to start and stop
        # from fraction through, to the end
        from_here = int( df.shape[0] // 2 )
        to_here = df.shape[0]

        # file name
        file_name = f'{your_file_name}_split_{file_counter}.csv'
        
        # make csv
        # drop (not in place) rows from_here to_here
        df.drop(df.index[from_here:to_here], inplace=False).to_csv( file_name, index=False, header=True ) 
        
        print("Made: ", file_name)

        # increment file counter
        file_counter += 1

        ##############
        # Second Half
        ##############
        # pick where to start and stop
        # from fraction through, to the end
        from_here = 0
        to_here = int( df.shape[0] // 2 )

        # file name
        file_name = f'{your_file_name}_split_{file_counter}.csv'
        
        # make csv
        # drop (not in place) rows from_here to_here
        df.drop(df.index[from_here:to_here], inplace=False).to_csv( file_name, index=False, header=True ) 
        
        print("Made: ", file_name)

        # increment file counter
        file_counter += 1

    return None

# iterate and make the requested number of files:
for i in range(0, number_of_reductions):
    # return both df and file_counter so changes are retained
    reduce_csv()

# print end
print("The End!!")
