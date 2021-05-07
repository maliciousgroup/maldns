import argparse

from pathlib import Path
from src.mutations import *
from src.misc import *
from timeit import default_timer as timer
from sys import exit


class MaliciousDNS(object):

    def __init__(self, domains: str, words: str, output: str):
        self.domains: list = self.return_list(domains)
        self.words: list = self.return_list(words)
        self.output: str = output

        if len(self.domains) == 0:
            print(f"{r}No domains were found in the provided file '{domains}'{rr}\n")
            exit(1)

        if len(self.words) == 0:
            print(f"{r}No words were found in the provided file '{words}'{rr}\n")
            exit(1)

        try:
            open(self.output, "w")
        except OSError as e:
            print(f"{color['red']}Error opening file '{self.output}' for writing")
            print(f"Exception:{color['reset']} {e.__str__()}\n")
            exit(1)

    @staticmethod
    def return_list(file: str) -> list:
        if Path(file).is_file():
            return [x.rstrip() for x in open(file, encoding='utf8')]
        return []

    def generate_permutations(self):

        print(f"Starting subdomain permutation process using {len(self.domains)} initial domains...\n")

        print(f"{m}[Stage 1]: Inserting provided words at each subdomain index...{rr}")
        start = timer()
        stage1: list = insert_all_indexes(self.domains, self.words)
        duration = round(timer() - start, 3)
        print(f"{m}[Stage 1]:{rr} {bb}Completed in {duration} seconds!{rr} (wrote {len(stage1)} results to file)\n")
        with open(self.output, "w") as wf:
            wf.write("\n".join(stage1))

        print(f"{m}[Stage 2]: Inserting provided numbers and dashes at each subdomain prefix/suffix index...{rr}")
        start = timer()
        stage2: list = insert_number_suffix(stage1)
        duration = round(timer() - start, 3)
        print(f"{m}[Stage 2]:{rr} {bb}Completed in {duration} seconds!{rr} (wrote {len(stage2)} results to file)\n")
        with open(self.output, "w") as wf:
            wf.write("\n".join(stage2))

        print(f"{m}[Stage 3]: Inserting provided words and dashes at each subdomain prefix/suffix index...{rr}")
        start = timer()
        stage3: list = insert_dashes(stage2, self.words)
        duration = round(timer() - start, 3)
        print(f"{m}[Stage 3]:{rr} {bb}Completed in {duration} seconds!{rr} (wrote {len(stage3)} results to file)\n")
        with open(self.output, "w") as wf:
            wf.write("\n".join(stage3))


if __name__ == "__main__":
    intro()
    # noinspection PyTypeChecker
    parser = argparse.ArgumentParser(add_help=False, usage=usage)

    parser.add_argument('-d', '--domains', action='store', dest='domains', default='', required=True)
    parser.add_argument('-w', '--words', action='store', dest='words', default='', required=True)
    parser.add_argument('-o', '--output', action='store', dest='output', default='', required=True)
    arg = None

    try:
        arg = parser.parse_args()
    except TypeError:
        usage()
        exit(f"{r}Invalid OR missing required options{rr}\n")

    o = MaliciousDNS(arg.domains, arg.words, arg.output)
    o.generate_permutations()
