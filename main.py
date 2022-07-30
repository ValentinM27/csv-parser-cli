import csv, json, sys
import os.path
from os import path

def main():
    # Test number of args
    if len(sys.argv) > 3 or len(sys.argv) < 3:
        print("Wrong number of arguments \n [csv file path] [json file path]")
        return 1

    # Check if path exists for CSV
    if path.exists(sys.argv[1]) != True:
        print("Path for document doesn't exist")
        return 1

    # Check if path for json exists
    head, tail = os.path.split(sys.argv[2])
    if len(head) > 0 and path.exists(head) != True:
        print("Wrong path for json")
        return 1

    # Open csv file
    data = {}
    with open(sys.argv[1]) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for i, row in enumerate(csv_reader):
            if 'id' in row:
                id = row['id']
            else:
                id = i
            data[id] = row

    # Create JSON file
    with open(sys.argv[2], 'w') as json_file:
        json_file.write(json.dumps(data, indent=4))

    print("file generated at " + sys.argv[2])
    return 0

if __name__== "__main__":
   main()
