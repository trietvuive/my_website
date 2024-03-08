import glob
import os

files = glob.glob('*.jpg')

i = 1
for file in files:
    filename = os.fsdecode(file)
    new_filename = str(i) + '.jpg'
    os.rename(filename, new_filename)
    i += 1

