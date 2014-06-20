#! /usr/bin/env python
# phonebook.py
# David Prager Branner
# 20140620

"""Create simple command-line phonebook application."""

import sys
import inspect
import sqlite3

def main(args):
    command = args[0]
    if command in commands:
        commands[command](args)
    else:
        print('No recognized command; exiting.')
        sys.exit()

def create(args):
    name_function()

def lookup(args):
    name_function()

def add(args):
    name_function()

def change(args):
    name_function()

def remove(args):
    name_function()

def reverse(args):
    name_function()

def name_function():
    print('You have called function {}'.format(inspect.stack()[1][3]))

commands = {'create': create,
        'lookup': lookup,
        'add': add,
        'change': change,
        'remove': remove,
        'reverse-lookup': reverse,
        'reverse': reverse,
        }

if __name__ == '__main__':
    args = sys.argv[1:]
    if len(args) > 4:
        print('Too many arguments; exiting.')
    elif args == []:
        print('Too few arguments; exiting.')
    else:
        main(args)
