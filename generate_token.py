#!/usr/bin/env python3

from argparse import ArgumentParser

import IPython as ipy

parser = ArgumentParser()
parser.add_argument(
    "-p",
    "--password",
    dest="password",
    help="The password you want to use for authentication.",
    required=True,
)
parser.add_argument(
    "--verbose",
    "-v",
    dest="verbose",
    default=0,
    action="count",
    help="Display extra information.",
    required=False,
)
args = parser.parse_args()

if args.verbose:
    print("Copy this line into the .env file:")

hash = ipy.lib.passwd(args.password)
print("ACCESS_TOKEN=" + hash)
