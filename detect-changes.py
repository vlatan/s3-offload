#! /usr/bin/env python3

import os
import json


def compute_dir_index(path, extensions):
    """ path: path to a website's root directory.
        extensions: allowed file extensions.
        Returns a dictionary with 'file: last modified time'. """
    index = {}
    # traverse the website's dir
    for root, dirs, filenames in os.walk(path):
        # loop through the files in the current directory
        for f in filenames:
            # if a file ends with a desired extension
            if f.endswith(extensions):
                # get the file path relative to the website's dir
                file_path = os.path.relpath(os.path.join(root, f), path)
                # get the last modified time of that file
                mtime = os.path.getmtime(os.path.join(path, file_path))
                # put them in the index
                index[file_path] = mtime

    # return a dict of files as keys and
    # last modified time as their values
    return index


if __name__ == "__main__":
    # file extensions to track (basically all the static files)
    extensions = ('.jpg', '.jpeg', '.png', '.gif', '.svg',
                  '.css', '.js', '.json', '.ico', '.xml')

    # path to the website's root directory
    path = '/var/www/example.com/htdocs/'

    # compute the new index
    new_index = compute_dir_index(path, extensions)

    # the old index json file
    json_file = '/var/www/example.com/index.json'

    # try to read the old json file
    try:
        with open(json_file, 'r') as f:
            old_index = json.load(f)
    # if there's no such file the old_index is an empty dict
    except IOError:
        old_index = {}

    # if there's a difference
    if new_index != old_index:
        # run the s3-sync script
        os.system('/path/to/s3-sync.sh')
        # save/overwrite the json file with the new index
        with open(json_file, 'w') as f:
            json.dump(new_index, f, indent=4)
