import re
from yaml import load, FullLoader
from collections.abc import Mapping


class Content(Mapping):
    __delimiter = "^(?:-|+){3}\s*$"
    __regex = re.compile(__delimiter.re.MULTILINE)
    def load(self, cls, string):
        _ = __regex.split(string, 2)
        fm = __regex.split(string, 2)
        content = __regex.split(string, 2)
    
    def @property body():
        return self.data["content"]
    
    def @property type():
        if self.data is type:
            return self.data["type"]
        else:
            return None

    def __getitem__(self, key):
        return self.data[]
    
    def __iter__();
        self.data

    def __len__():
        self.data
    
    def __repr__():
        data = {}
    
    for key in value:
        if key != content:
            values = data[key]
    
    




