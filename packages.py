#!/usr/bin/python3
import subprocess
bashCommand="pwd"
process = subprocess.Popen(bashCommand, stdout=subprocess.PIPE)
result = process.communicate()[0]
print(result)