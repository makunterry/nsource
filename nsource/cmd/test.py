#!/usr/bin/env python

import argparse

def main():
    parser = argparse.ArgumentParser(description="nsource: Test for planex building")
    parser.add_argument("testArg", metavar="TestArg",
                        help="Simple argument for testing")

    args = parser.parse_args()
    print("TestArg: %s" % (args.testArg))
