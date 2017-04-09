import csv
import sys
import os
DATASET_PATH=os.path.join(os.path.dirname(__file__),"datasets","ml-latest-small","ratings.csv")
f = open(DATASET_PATH, 'r')
try:
    reader = csv.reader(f)

    for row in reader:
        print row
finally:
    f.close()