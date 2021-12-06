# -*- coding: utf-8 -*-

"""
Requires: pandas as pd


2021.12.06
This is a Python script to make split .csv files into 
an even number of split files (2, 4, 6, etc.)
that collectively contain all of the data.

For example, if one file is too big, and you want to make
four smaller files that contain all the data.

Your select the number of files you want each file split into.

This will automatically split all files in the directory
the specified number of times.

For example:
Running this script two times, each time set to: 2 (resulting files)
is the same as running this script one time, set to 4 (resulting files).
"""

import pandas as pd
import os
import glob
# from datetime import datetime


# helper function 
def remove_split_from_name(name):
    """
    if last part of name is _split__###
    return: name - "split"

    Else, return: name
    """
    if name[-15:-7] == "_split__":
        return name[:-15] + ".csv"
    else:
        return name

# helper function to make name
def make_new_names(name):
    """this splits the name into the next two split number
    1 -> 1, 2
    x*2-1, x*2
    plus padding
    """
    # look for if the name is already split
    if name[-15:-7] == "_split__":

        # extract old number
        three_numbers = int( name[-7:-4] )

        # new numbers
        new_first_file_number = (three_numbers * 2) - 1
        new_second_file_number = (three_numbers * 2)

        # get number of digits
        first_number_of_digits = len( str( new_first_file_number ) )
        second_number_of_digits = len( str( new_second_file_number ) )

        name_root = remove_split_from_name( name )[:-4]

        if first_number_of_digits == 3:
            first_new_name = f'{name_root}_split__{new_first_file_number}.csv'
            second_new_name = f'{name_root}_split__{new_first_file_number}.csv'
    

        if first_number_of_digits == 1:
            first_new_name = f'{name_root}_split__0{new_first_file_number}.csv'
        if second_number_of_digits == 2:
            second_new_name = f'{name_root}_split__0{new_second_file_number}.csv'


        if first_number_of_digits == 1:
            first_new_name = f'{name_root}_split__00{new_first_file_number}.csv'
        if second_number_of_digits == 1:
            second_new_name = f'{name_root}_split__00{new_second_file_number}.csv'

        return first_new_name, second_new_name

    else:
        # if the file is original, leave the new name 
        # as _split__001 or _split__002
        first_new_name = f'{name[:-4]}_split__001.csv'
        second_new_name = f'{name[:-4]}_split__002.csv'
        return first_new_name, second_new_name



def split_csv():

    # date_time = datetime.utcnow()
    # timestamp = date_time.strftime('%Y_%m_%d_%H_%M_%S_%MS')
    # os.mkdir( timestamp )

    # get list of csv files
    file_list = glob.glob("*.csv")

    # # inspection
    # print("first", file_list)

    ########################################################
    # reverse order of list, to avoid over-writing of files
    ########################################################
    # sort list
    file_list.sort()

    # # inspection
    # print("sort 1", file_list)

    # reverse order
    file_list = file_list[::-1]

    # # inspection
    # print("reverse", file_list)

    # iterate through list of csv files
    for your_file_name in file_list:

        file_counter = 1

        # load csv into pandas
        df = pd.read_csv( your_file_name )

        # os.remove(your_file_name)

        #########################
        # New files names, 1 & 2
        #########################

        # TODO: if original file is a split -> delete it!

        first_new_file_name, second_new_file_name = make_new_names( your_file_name )

        #############
        # First Half
        #############
        # pick where to start and stop
        # from fraction through, to the end
        from_here = int( df.shape[0] // 2 )
        to_here = df.shape[0]
    
        # make csv
        # drop (not in place) rows from_here to_here
        df.drop(df.index[from_here:to_here], inplace=False).to_csv( first_new_file_name, index=False, header=True ) 

        print("Made: ", first_new_file_name)

        # increment file counter
        file_counter += 1

        ##############
        # Second Half
        ##############
        # pick where to start and stop
        # from fraction through, to the end
        from_here = 0
        to_here = int( df.shape[0] // 2 )

        # make csv
        # drop (not in place) rows from_here to_here
        df.drop(df.index[from_here:to_here], inplace=False).to_csv( second_new_file_name, index=False, header=True ) 
        
        print("Made: ", second_new_file_name)

        # increment file counter
        file_counter += 1

        ##################
        # rename original
        ##################
        if your_file_name[-15:-7] != "_split__":
            # rename...
            new_original_name = your_file_name + "_original"
            os.rename( your_file_name, new_original_name )

    return None


def main_split_csv_iterator():
    # flag
    file_ok = False

    # check to see if input number works, if not ask again
    while file_ok is False:

        try:
            # Ask how many files to split the file into?
            number_of_final_files = int( input("Files divided into how many pieces? (even number) \n ") )

            number_of_reductions = int( number_of_final_files / 2 )

            file_ok = True

        except:
            file_ok is False
            print("That did not work. Please try an even integer (like 2, 4, 6, etc.) \n")



    # iterate and make the requested number of files:
    for i in range(0, number_of_reductions):
        # return both df and file_counter so changes are retained
        split_csv()

    # print end
    return print("The End!!")

main_split_csv_iterator()


