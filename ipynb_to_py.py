#!/usr/bin/env python3

import json
import sys
import os

file_name = sys.argv[1]

if not os.path.exists(file_name):
    print("File not found")
    sys.exit(1)

assert file_name.endswith(".ipynb"),"Not a ipynb file"
data = {}

with open(file_name) as f:
    data = json.load(f)

source = ""
for i in data["cells"]:
    for j in i["source"]:
        source = source + j


print(source)

with open(file_name.replace("ipynb","py"),"w") as f:
    f.write(source)
