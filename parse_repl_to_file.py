#!/usr/bin/env python3

import sys
import uuid
import subprocess

repl_output_file = sys.argv[1]
file_contents    = None

with open(repl_output_file) as f:
    file_contents = f.read()

lines = [x.strip().strip("\t").removeprefix(">>> ").removeprefix("... ") 
        for x in file_contents.splitlines() if 
        (x.startswith(">>> ") or x.startswith("... ")) 
        and (x.strip().strip("\t").removeprefix(">>> ").removeprefix("... ")!="")
        ]
lines = [line.removeprefix(">>>").removeprefix("...") for line in lines]
lines = [line for line in lines if line.strip().strip("\t")!=""]

new_file_name = str(uuid.uuid4())[:5] + ".py"
f = open(new_file_name,"w")

for line in lines:
    print(line)
    f.write(line)
    f.write("\n")

f.close()
print()
print(f"File saved as `{new_file_name}`")

err = False
print("-"*20)
try:
    _ = subprocess.check_call(["/usr/bin/env", "python3", "-m", "py_compile", new_file_name])
    print("-"*20,end="")
    print("..ok")
except Exception as e:
    err = True
    print("-"*20)
    print(f"Possible Errors in Generated File `{new_file_name}`.. Check REPL output")
    print("-"*20)

