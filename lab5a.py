#!/usr/bin/env python3
# Author ID: rrakshit

def read_file_string(file_name):
    # Opens the file and reads its entire contents as a string
    try:
        with open(file_name, 'r') as f:
            return f.read()
    except Exception as e:
        return f"Error: {e}"

def read_file_list(file_name):
    # Opens the file and reads its contents as a list, removing newline characters
    try:
        with open(file_name, 'r') as f:
            return [line.strip() for line in f.readlines()]
    except Exception as e:
        return f"Error: {e}"

if __name__ == '__main__':
    file_name = 'data.txt'
    print(read_file_string(file_name))
    print(read_file_list(file_name))
