import os
import subprocess
from distutils.dir_util import copy_tree

def get_file_paths_with_same_name(directory_path, file_name):
    file_paths = []
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file == file_name:
                file_paths.append(os.path.join(root, file))
    return file_paths

build_scripts = get_file_paths_with_same_name(os.getcwd()+r"\patch", "build.bat")
output_dirs = []
for s in build_scripts:
    print(s)
    p = subprocess.Popen(s, stdout = subprocess.PIPE, cwd=s.replace(r"\build.bat", ""))
    stdout, stderr = p.communicate()
    output_dir = s.replace(r"\build.bat", r"\output")
    copy_tree(output_dir, "patchout")
    print()

copy_tree("patchout", r"ISO\unpacked\files\TM")