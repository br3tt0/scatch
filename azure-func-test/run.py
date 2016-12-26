import os

for var in os.environ:
    if var[:4] == 'REQ_':
        print("{} = {}".format(var, os.environ[var]))