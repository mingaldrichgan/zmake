import os
import shutil
import subprocess
import sys

from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
from zmake import VERSION

if os.path.isdir("dist"):
    shutil.rmtree("dist")
if os.path.isdir("build"):
    shutil.rmtree("build")

if sys.platform == "win32":
    pyinstaller = "./venv/Scripts/pyinstaller"
    spec_file = "zmake.win32.spec"
    result_file = "zmake.exe"
else:
    pyinstaller = "./venv/bin/pyinstaller"
    spec_file = "zmake.linux.spec"
    result_file = "zmake"

# Build
subprocess.Popen([pyinstaller, spec_file]).wait()

os.symlink("../zmake/zmake.json", "dist/zmake.json")
os.symlink("../zmake/data", "dist/data")
