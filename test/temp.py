import os
import pathlib
from glob import glob
from pathlib import Path

output = [name for name in os.listdir('..') if os.path.isdir(os.path.join('..', name))]
filtered_output = [dir for dir in output if dir in ['XRAY','CT','analyze']]
print(output)