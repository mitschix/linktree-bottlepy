#!/usr/bin/env python

# generate token with key + timestamp -> md5
from datetime import date
from sys import argv
import hashlib
import argparse
from userdata import TOKEN_KEY, USER_URL

# init the command line argument parser
parser = argparse.ArgumentParser()

# get default key from user data file -> if none is set key to "testkey"
if TOKEN_KEY:
    parser.add_argument(
        "key",  default=TOKEN_KEY, nargs="?", type=str, help="Key used to generate the token.")
else:
    parser.add_argument(
        "key",  default="testkey", nargs="?", type=str, help="Key used to generate the token.")

parser.add_argument(
    "-u", "--url", action="store_true", help="Print the url to your linktree + token.")
parser.add_argument(
    "-t", "--token", action="store_true", help="Write the token into the token file.")

args = parser.parse_args()


def create_token(ky):
    timestamp = date.today().strftime("%B%d,%Y")
    tmp = f"{timestamp}{ky}"
    hashed = hashlib.md5(tmp.encode()).hexdigest()
    tmp_1 = hashed[:14]
    tmp_2 = hashed[21:]
    token = f"{tmp_2}{tmp_1}"
    return token


def print_url(token):
    print(f"{USER_URL}?at={token}")


def write_token(token):
    with open("token_file", 'w') as wf:
        wf.write(token)


if __name__ == "__main__":
    token = create_token(args.key)
    if args.url:
        print_url(token)
    if args.token:
        write_token(token)
