from src.colors import *
from sys import argv


def intro():
    data: str = f"""
{color['magenta']}
███╗   ███╗ █████╗ ██╗     ██████╗ ███╗   ██╗███████╗
████╗ ████║██╔══██╗██║     ██╔══██╗████╗  ██║██╔════╝
██╔████╔██║███████║██║     ██║  ██║██╔██╗ ██║███████╗
██║╚██╔╝██║██╔══██║██║     ██║  ██║██║╚██╗██║╚════██║
██║ ╚═╝ ██║██║  ██║███████╗██████╔╝██║ ╚████║███████║
╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝╚═════╝ ╚═╝  ╚═══╝╚══════╝{color['reset']}
                                             v1-alpha
                                      malicious.group

{m}Author:{rr} d3d ({b}@MCoetus{rr})
{m}Credit:{rr} {b}@infosec_au{rr} for originally writing the permutation functions in 'altdns'

"""
    print(data)


def usage() -> None:
    output: str = f"""{color['magenta']}{argv[0]} Options:{color['reset']}
  '-d', '--domains'     - Set the domain or file containing domains used in permutations
  '-w', '--words'       - Set the words that you'd like to permute with your current domains
  '-o', '--output'      - Set the output filename and location to store results
"""
    print(output)
