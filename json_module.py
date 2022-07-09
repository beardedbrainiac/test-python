import json
import os
import json

def reader(file_name):
    path_to_json = os.path.join(os.path.dirname(os.path.abspath(__file__)), file_name)
    f = open(path_to_json, encoding="utf8")

    # returns JSON object as
    # a dictionary
    data = json.load(f)

    return data

def writer(file_name, json_object):
    # Writing to sample.json
    with open(file_name, "w", encoding="utf8") as outfile:
        json.dump(json_object, outfile, ensure_ascii=False)