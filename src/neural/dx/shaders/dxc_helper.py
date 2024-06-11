#!/usr/bin/env python
# Call dxc with absolute paths where '/' are converted to '\' (in windows).
import os
import re
import sys

x = sys.argv
x.pop(0)
for i in range(len(x)):
    if re.match(r"[a-zA-Z]:/", x[i]):
        x[i] = os.path.normpath(x[i])
# We asssume dxc is already on the path.
os.system("dxc " + '"{}"'.format('" "'.join(x)))
