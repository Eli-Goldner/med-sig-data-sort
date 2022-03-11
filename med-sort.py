import os
import csv
import shutil
import argparse

parser = argparse.ArgumentParser(description='Create train dev test splits for DeepPheCR csvs')
parser.add_argument('--split_dir', type=str, help='Directory containing csvs with filepaths')
parser.add_argument('--med_system_dir', type=str)

def correct_xml(filename):
    # Only looking for files which have been annotated by David Harris
    return filename.split('.')[-3] == 'dave'
            
def main(split_dir, med_system_dir):
    xml_path_key = 'path to gold annotations on anafora server'
    for filename in os.listdir(split_dir):
        with open(os.path.join(split_dir, filename), mode ='r') as in_file:
            # reading the CSV file
            csvFile = csv.DictReader(in_file)
            for row in csvFile:
                anafora_dir = row[xml_path_key].split('/')[-1]
                split_portion = filename.split('_')[0]
                src_dir = os.path.join(med_system_dir, anafora_dir, row['file'], "")
                for ann_file in os.listdir(src_dir):
                    ann_filename = os.path.basename(ann_file)
                    target_dir = os.path.join(med_system_dir, split_portion, "")
                    ann_filepath = os.path.join(src_dir, ann_file)
                    if ann_filename.endswith('xml'):
                        if correct_xml(ann_filename):
                            final_target = os.path.join(target_dir, "gold", "")
                            shutil.copy(ann_filepath, final_target)
                    else:
                        final_target = os.path.join(target_dir, "text", "")
                        shutil.copy(ann_filepath, final_target)
                        old_ann_filename = os.path.join(final_target, ann_filename)
                        new_ann_filename = os.path.join(final_target, f"{ann_filename}.txt")
                        os.rename(old_ann_filename, new_ann_filename)
                        
if __name__=='__main__':
    args = parser.parse_args()
    main(args.split_dir, args.med_system_dir)
