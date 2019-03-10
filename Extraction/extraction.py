import os
import re
import numpy as np

# change it to your own directory that contains all the data
directory = '/Users/xmliszt1/Desktop/Extraction/Results'

def extraction(fileobject = ''):
    f = open(fileobject,'r')
    fr = f.read()
    lst = fr.split(";")
    string = lst[1]
    PW = re.findall('PW\[(\d*)', string)
    PB = re.findall('PB\[(\d*)', string)
    RE = re.findall('RE\[(.*)\]', string)

    output = list()
    output.append("PW: {0}".format(PW))
    output.append("PB: {0}".format(PB))
    output.append("RE: {0}".format(RE))
    return output

def change_format_to_txt(directory = ''):
    for filename in os.listdir(directory):
        if filename.endswith(".sgf"):  # here change it to any extension of your file
            base = os.path.splitext(filename)[0]
            path = os.path.join(directory, filename)
            os.rename(path, base + ".txt") # convert the extension to .txt

change_format_to_txt(directory = directory)

output = list()
for filename in os.listdir(directory):
    full_path = os.path.join(directory, filename)
    output.append(extraction(fileobject= full_path))

a = np.asarray(output)
print(np.asarray(output))
np.savetxt("results.csv", a , fmt = "%s")