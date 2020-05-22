from time import time
from operator import itemgetter
import datetime
import os
import os.path
import string
import hashlib
import sys
import yaml,json

class ScanHelper:
    def __init__(self):
        pass

    def loopDir(self, dirname, outputdir):
        for rt, dirs, files in os.walk(dirname):
            for f in files:
                if (f.find(".yaml") == -1):
                    continue

                with open(os.path.join(outputdir, os.path.splitext(f)[0]+".json"), "w") as json_file:
                    fname = os.path.join(rt, f)
                    with open(fname, "rt") as yaml_file:
                        file_length = os.path.getsize(fname)
                        document = yaml_file.read(file_length)
                        json.dump(yaml.load(document), json_file)
                        print("\t " + f  + " has turned to " + os.path.splitext(f)[0]+".json")

                # break

if __name__ == "__main__":
    try:
        outputfolder = sys.argv[1]  #yaml2json.py outputfolder inputfolder
    except:
        outputfolder = "./"

    try:
        inputfolder = sys.argv[2]
    except:
        inputfolder = "./"

    ss = ScanHelper()
    ss.loopDir(inputfolder, outputfolder)
print("done")
