import os
import csv
import argparse

parser = argparse.ArgumentParser(description='Interpolate correct DocTimeRels in system output.')
parser.add_argument('--split_dir', type=str, help='System output file requiring DocTimeRels')
parser.add_argument('--out_dir', type=str)

# opening the CSV file
def main(split_dir, out_dir):
    for filename in os.listdir(split_dir):
        with open(filename, mode ='r') as file:
            # reading the CSV file
            csvFile = csv.DictReader(file)
	    if filename.startswith('train'):
	        pass
            elif filename.startswith('test'):
	        pass
            elif filename.startswith('dev'):
	        pass
 

if __name__=='__main__':
    args = parser.parse_args()
    main(args.split_dir, args.out_dir)
