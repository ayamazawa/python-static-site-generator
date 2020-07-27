from pathlib import Path

class Site:
    def __init__(self, source, dest):
        self.source = Path(source)
        self.dest = Path(dest)
        
    def create_dir(self, path):
        directory = self.dest / path.relative_to(self.source)
        directory.mkdir(parents=True, exist_ok=True)
    

    def build(self):
        self.dest.mkdir(parents=True, exist_ok=True)
        for path in self.source.rglob("*"):
            if path.is_dir():
                self.create_dir(path)
            elif path.is_file():
                run_parser(path)

    parsers = None

    def load_parser(extension):
        for parser in self.parsers:
            if extension is valid_extensions():
                return parser
    
    def run_parser(path):
        parser = load_parser(path.suffix)
        if parser is not None:
            parse(path,source,dest)
        else:
            NotImplemented
    
