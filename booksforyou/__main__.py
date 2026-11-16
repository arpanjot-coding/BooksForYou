import argparse
import sys

from .app import run


def main(argv=None):
    parser = argparse.ArgumentParser(
        prog="booksforyou",
        description="Pick a random free, public-domain book.",
        allow_abbrev=False,
    )
    parser.parse_args(argv)
    return run()


if __name__ == "__main__":
    sys.exit(main())
