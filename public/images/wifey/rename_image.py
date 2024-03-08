import glob
import os

os.chdir('C:\\Users\\vomin\\Documents\\image')
files = glob.glob('*.jpg')
files.sort(key=os.path.getmtime)

i = 1
for file in files:
    filename = os.fsdecode(file)
    new_filename = str(i) + '.jpg'
    os.rename(filename, new_filename)
    i += 1


