"""
Script Name: read_file.py
Description: Reads a file and prints its contents.
"""

import sys

def read_file(filename):
    """Reads a file and prints its contents."""
    try:
        with open(filename, "rw", encoding="utf-8") as file:
            print(file.read())
    except FileNotFoundError:
        print(f"Error: {filename} not found.")

if __name__=="__main__":
    if len(sys.argv) != 2:
        print("Usage: python read_file.py <filename>")
    else:
        read_file(sys.argv[1])