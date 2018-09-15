from argparse import ArgumentParser, FileType, RawDescriptionHelpFormatter

from . import doc_split, usage, version
from .mutalyzer_client import *


def mutalyzer_client():
    """
    """
    pass


def main():
    """Main entry point."""
    parser = ArgumentParser(
        formatter_class=RawDescriptionHelpFormatter,
        description=usage[0], epilog=usage[1])
    parser.add_argument('-v', action='version', version=version(parser.prog))

    try:
        args = parser.parse_args()
    except IOError as error:
        parser.error(error)

    try:
        mutalyzer_client(
            **{k: v for k, v in vars(args).items()
            if k not in ('func', 'subcommand')})
    except (ValueError, IOError) as error:
        parser.error(error)


if __name__ == '__main__':
    main()