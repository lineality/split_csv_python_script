# -*- coding: utf-8 -*-

"""
2021.12.13
Requires: pandas as pd

inputs: main_split_csv_iterator(threshold = None, 
                                number_of_splits = None, 
                                combine = False)
you can pick any of these 3 inputs, but one more than one.
inputs must be put in when calling .py script, not from input-prompt.

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


There are there types of user input: 
1. a threshold size, where any .csv file larger than that
threshold will be split
2. number of times to split all files. This is NOT the number of resulting
files, but the number of splits. e.g.
number of splits: 1  2  3   4   5
number of files:  2  4  8  16  32
3. combine = True 
to recombine split files

"""

import pandas as pd
import os
import glob


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

    this program deals with the reading and updating 
    the number of the split file
    making he new number based on the old number
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

        # get name separate from ".csv"
        name_root = remove_split_from_name( name )[:-4]

        # looking at files with a hundreds number
        if first_number_of_digits == 3:
            first_new_name = f'{name_root}_split__{new_first_file_number}.csv'
            second_new_name = f'{name_root}_split__{new_first_file_number}.csv'
    

        if first_number_of_digits == 2:
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

# helper function
def combine_csv():

    # glob all csv files
    remaining_csv_list = glob.glob("*.csv")

    # make new name: output .csv name
    old_name = remaining_csv_list[0]
    new_name = old_name[:-15] + ".csv"

    # sort all files
    remaining_csv_list.sort()

    # open the first file
    df = pd.read_csv(remaining_csv_list[0])

    # remove first file from list
    remaining_csv_list.pop(0)

    # iterate through remaining files
    for this_file in remaining_csv_list:

        print("and I combined THIS file", this_file, "!")

        # load next file
        df2 = pd.read_csv(this_file)

        # combine dataframes
        df = df.append(df2)

        # reset index
        df.reset_index(drop=True, inplace=True)

    # output new combined file
    df.to_csv(new_name)

    print("All Done! -> ", new_name)


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
        # try alt encoding if default does not work
        try:
            df = pd.read_csv( your_file_name )

        except:
            df = pd.read_csv( your_file_name , encoding = "ISO-8859-1" )

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
        from_here = int( df.shape[0] // 2 ) - 1
        to_here = df.shape[0]
    
        # make csv
        # drop (not in place) rows from_here to_here
        df.drop(df.index[from_here:to_here], inplace=False).to_csv( first_new_file_name, index=False, header=True ) 

        print("Made: ", first_new_file_name, "shape = ", to_here - from_here)

        # increment file counter
        file_counter += 1

        ##############
        # Second Half
        ##############
        # pick where to start and stop
        # from fraction through, to the end
        from_here = 0
        to_here = int( df.shape[0] // 2 ) - 1

        # make csv
        # drop (not in place) rows from_here to_here
        df.drop(df.index[from_here:to_here], inplace=False).to_csv( second_new_file_name, index=False, header=True ) 
        
        print("Made: ", second_new_file_name, "shape = ", to_here - from_here)

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


# helper function
def check_threshold_OK_is_True_or_get_split_number( df, threshold ):

    under_threshold_flag = False

    number_of_rows_in_file = df.shape[0]

    # check if shape is under threshold
    if df.shape[0] < threshold:

        # set flag
        under_threshold_flag = True

        # for terminal
        print("threshold = ", threshold)
        print("number_of_rows_in_file = ", number_of_rows_in_file)
        print("csv file size in under threshold! OK!")

        # return true
        return True
    
    if under_threshold_flag is False: 

        # determine how many splits will be under threshold
        
        # starting values (one file, zero splits)
        number_of_csv_files = 1
        number_of_splits = 0

        # over-estimate later files being slightly bigger
        # number added may need to be adjusted
        while ((number_of_rows_in_file / number_of_csv_files) + (number_of_splits)) > threshold:

            # double the split-number
            number_of_splits += 1
            number_of_csv_files *= 2
        
            # print("number_of_rows_in_file / number_of_csv_files = ", number_of_rows_in_file / number_of_csv_files)
            # print("threshold = ", threshold)
            # print("over threshold boolean = ", ((number_of_rows_in_file / number_of_csv_files) + (number_of_splits * 3)) > threshold)
            print("number_of_splits = ", number_of_splits)
            print("number_of_csv_files = ", number_of_csv_files)
            # print('\n')

        return number_of_splits

def main_split_csv_iterator(threshold = None, number_of_splits = None, combine = False):

    # flag
    input_format_ok = False

    # check to see if input number works, if not ask again
    while input_format_ok is False:

        try:
            user_input = input("Say a split number or 'threshold' or 'combine'")

            if user_input == 'threshold':
              threshold = True
              input_format_ok = True

            elif user_input == 'combine':
                combine = True
                input_format_ok = True

            else: 
                # Ask how many files to split the file into?
                number_of_splits = int( user_input )

                input_format_ok = True

        except:
            input_format_ok is False
            print("That did not work. Please try an even integer (like 1,2,3 etc.) or 'combine' or 'threshold'\n")

    ####################
    # Choose your path!
    ####################

    if combine != False:
        # run combine_csv
        combine_csv()
        return print("split-files were recombined. Finished.")

    elif (threshold != None) and (number_of_splits != None):
        
        return print("Error: You cannot use threshold and numbe of splits together. Please try again.")

  
    elif threshold != None:

        # flag
        input_format_ok = False

        # check to see if input number works, if not ask again
        while input_format_ok is False:

            try:
                user_input = input("Set your threshold:")


                # Ask how many files to split the file into?
                threshold = int( user_input )

                input_format_ok = True

            except:
                input_format_ok is False
                print("That did not work. Please try an integer (like 2, 4, 6, etc.)")


        # make list of files
        csv_list = glob.glob("*.csv")

        # iterating through list of files to estimate needed number of splits:
        for this_file in csv_list:

            # load .csv into pandas df
            # try alt encoding if default does not work
            try:
                df = pd.read_csv( this_file )
            except:
                df = pd.read_csv( this_file , encoding = "ISO-8859-1" )

            number_of_splits = check_threshold_OK_is_True_or_get_split_number( df, threshold )

            # inspection
            print("number_of_splits", number_of_splits)

            if number_of_splits != True:

                # iterate and make the requested number of files:
                for i in range(0, number_of_splits):
                    # return both df and file_counter so changes are retained
                    print("splitting...")
                    split_csv()


    elif number_of_splits != None:

        # iterate and make the requested number of files:
        for i in range(0, number_of_splits):
            # return both df and file_counter so changes are retained
            split_csv()

        # print end
        return print("The End!!")




main_split_csv_iterator()

