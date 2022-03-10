import os
import csv
import argparse
from pathlib import Path

parser = argparse.ArgumentParser(description='Create train dev test splits for DeepPheCR csvs')
parser.add_argument('--split_dir', type=str, help='Directory containing csvs with filepaths')
parser.add_argument('--out_dir', type=str, help='Directory to output the splits')

# opening the CSV file
def main(split_dir, out_dir):
    txt_path_key = 'path to the file'
    xml_path_key = 'path to gold annotations on anafora server'
    for filename in os.listdir(split_dir):
        with open(filename, mode ='r') as in_file:
            # reading the CSV file
            csvFile = csv.DictReader(in_file)
            text_path = csvFile[txt_path_key]
            xml_path = csvFile[xml_path_key]
            split_out = filename.split('_')[0]
            out_subdir = Path(out_dir + '/' + split_out)
            out_subdir.mkdir(parents=True, exist_ok=True)
            out_path = out_subdir / csvFile['patient ID'] 
            with out_path.open("w", encoding ="utf-8") as out_file:
                pass
            
if __name__=='__main__':
    args = parser.parse_args()
    main(args.split_dir, args.out_dir)
