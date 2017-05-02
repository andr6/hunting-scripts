import r2pipe
import argparse

TARGET = "/bin/ls"
MODES = ['imports', 'symbols', 'strings', 'file_info']

class R2Recon():
    def __init__(self, target, mode):
        self.target = target
        self.mode = mode
        self.result = []
        self.r2p = r2pipe.open(TARGET)

    def imports(self, target):
        """
        Gather information on imports
        """
        result = self.r2p.cmdj('iij')

        for item in result:
            print("[{}]: \t{}\t\t\t({})".format(
                item['type'], item['name'], item['bind']))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("target",
                        metavar="TARGET",
                        action="store",
                        help="Target file to perform recon against")

    parser.add_argument("--file",
                        dest="in_file",
                        action="store",
                        help="File to read search strings from.")
