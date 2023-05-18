import os
import json
import csv
import pickle


def get_dir_info(dir_path):
    dir_info = {}
    dir_size = 0
    for root, dirs, files in os.walk(dir_path):
        for d in dirs:
            sub_dir_path = os.path.join(root, d)
            sub_dir_info, sub_dir_size = get_dir_info(sub_dir_path)
            dir_info[sub_dir_path] = {'type': 'directory', 'size': sub_dir_size, 'parent': root}
            dir_info.update(sub_dir_info)
            dir_size += sub_dir_size
        for f in files:
            file_path = os.path.join(root, f)
            file_size = os.path.getsize(file_path)
            dir_info[file_path] = {'type': 'file', 'size': file_size, 'parent': root}
            dir_size += file_size
    return dir_info, dir_size


def save_json(dir_info, file_name):
    with open(file_name, 'w') as f:
        json.dump(dir_info, f)


def save_csv(dir_info, file_name):
    with open(file_name, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['path', 'type', 'size', 'parent'])
        for path, info in dir_info.items():
            writer.writerow([path, info['type'], info['size'], info['parent']])


def save_pickle(dir_info, file_name):
    with open(file_name, 'wb') as f:
        pickle.dump(dir_info, f)


dir_path = 'F:\GeekBrains\pythonfull\DZ'
dir_info, dir_size = get_dir_info(dir_path)
save_json(dir_info, 'dir_info.json')
save_csv(dir_info, 'dir_info.csv')
save_pickle(dir_info, 'dir_info.pickle')
