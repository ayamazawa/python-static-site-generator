from typing import List
from pathlib import Path
import shutil

class Parser:
    extensions = List[str]
    def valid_extension(self, extension):
        if extension is in self.extensions:
            return extension
    
    def parse(path, source, dest):
        raise NotImplementedError

    def read(path):
        with open(path):
            return read(file)
    
    def write(path,dest,content,ext=".html"):
        full_path = "self.dest/with_suffix(ext).name"
        return full_path
        with open(full_path):
            content = write(file)

    def copy(path,source,dest):
        shutil.copy2(path,full_path)
    
    def ResourceParser():
        self.extensions = ["*.jpg", ".png", ".gif", ".css", ".html"]
        parse(self)
        copy(path,source,dest)
        



    




