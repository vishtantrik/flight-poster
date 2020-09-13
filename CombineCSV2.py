path_to_search = './Data/Raw/Flight_Tracks/*.csv'
path_to_output = './Data/Processed/Flight_Tracks_Consolidated.csv'
expected_header = 'Timestamp,UTC,Callsign,Position,Altitude,Speed,Direction\n'
col_to_add = 'Filename'

import glob
import os
i=0
data_strings_all = []
new_header = col_to_add + "," + expected_header

# Get paths of all CSV files
file_paths = glob.glob(path_to_search)

# Verify that there are no copies
#  Check files names for repeats after removing " - Copy" and " (/d+)"

# For each file
for fpath in file_paths:
    fname = os.path.basename(fpath)
    fname_wo_ext = os.path.splitext(fname)[0]
    # print(f'Processing file number {i}: {fname}')

    i = i + 1

    # Open File
    fobj = open(fpath, 'r')

    # Verify Header
    header = fobj.readline()
    if header == expected_header:
        # Get CSV Data
        data_strings = fobj.readlines()
        # Add "Filename" column to data
        data_strings = [fname_wo_ext + "," + data_string for data_string in data_strings]
        # Append data to consolidated dataset
        data_strings_all = data_strings_all + data_strings
    else:
        print(f' file number {i}: {fname}, Header is not as expected')

    fobj.close()

# Write to file
out_fobj = open(path_to_output, 'w')
out_fobj.write(new_header)
out_fobj.writelines(data_strings_all)
out_fobj.close()