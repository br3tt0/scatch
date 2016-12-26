import os

for var in os.environ:
    print("{} = {}".format(var, os.environ[var]))