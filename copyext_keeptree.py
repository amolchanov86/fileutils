#!/usr/bin/env python

import argparse
import sys
import fileutils as fu


## Tests functionality
def main(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "src_dir",
        help="Input directory"
    )
    parser.add_argument(
        "dest_dir",
        help="Input directory"
    )
    parser.add_argument(
        "ext",
        help="Extension of files to filter"
    )
    parser.add_argument(
        "-v","--verbose",
        action="store_true",
        help="Extension of files to filter"
    )

    args = parser.parse_args()
    extensions = args.ext.split(',')

    print fu.copyext_keeptree(args.src_dir, args.dest_dir, extensions, args.verbose)

if __name__ == '__main__':
    main(sys.argv)
