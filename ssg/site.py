import Path from pathlib

class Site(self,source,dest):
    self.source = Path()
    self.dest = Path()
    def create_dir(self,path):
        directory = self.dest / relative_to(self.source)
        mkdir(directory,parents=True,exist_ok=True)
    def build():
        mkdir(self.dest,parents=True,exist_ok=True)
        for path in self.source.rglob("*"):
            create_dir(path)
        



