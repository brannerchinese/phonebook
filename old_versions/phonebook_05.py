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
    if args[-1].split('.') == 'pb':
        database = args[-1]
    else:
        database = 'hsphonebook.pb'
    if command in commands:
        # Creates database if not already existing.
        connection = sqlite3.connect(database)
        with connection:
            result = commands[command](args, connection)
        if result:
            print('created phonebook {} in the current directory'.
                    format(database))
    else:
        print('No recognized command; exiting.')
        sys.exit()

def create(args, connection):
    try:
        connection.execute('DROP TABLE IF EXISTS records;')
        # Note that assignment implies names must be unique.
        connection.execute('''CREATE TABLE records (
              name TEXT UNIQUE,
              numb TEXT
              );''')
    except sqlite3.Error as e:
        print('Error in creating database:\n    {}'.format(e))
        sys.exit()
    return True

def lookup(args, connection):
    # Look up args[1] in records.name.
    try:
        cursor = connection.execute('''SELECT name,numb FROM records '''
                '''WHERE name LIKE ?''', ('%' + args[1] + '%',))
    # Catch error if args[1] is not unique.
    except sqlite3.Error as e:
        print('Unexpected SQLite3 error:\n{}'.format(e))
    # List results.
    results = cursor.fetchall()
    if results:
        for item in results:
            print(item[0], item[1])
    # Report if name not found.
    else:
        print('Name {} not found.'.format(args[1]))

def add(args, connection):
    # Attempt to add args[1] as name and args[2] as numb.
    try:
        connection.execute('''INSERT INTO records (name,numb) '''
                '''VALUES (?,?)''', (args[1], args[2]))
    # Catch error if args[1] is not unique.
    except sqlite3.IntegrityError as e:
        print('Name "{}" already exists; duplicates not permitted.'.
                format(args[1]))
    # Report results.
    else:
        print('Added name {} and number {}.'.
                format(args[1], args[2]))


def change(args, connection):
    name_function()
    # Attempt to update args[2] as numb for args[1] as name.
    # Catch error if args[1] does not exist.

def remove(args, connection):
    name_function()
    # Attempt to remove record for args[1] as name and args[2] as numb.
    # Catch error if args[1] does not exist.

def reverse(args, connection):
    # Look up args[1] in records.num.
    try:
        cursor = connection.execute('''SELECT name,numb FROM records '''
                '''WHERE numb LIKE ?''', ('%' + args[1] + '%',))
    except sqlite3.Error as e:
        print('Unexpected SQLite3 error:\n{}'.format(e))
    # List results.
    results = cursor.fetchall()
    if results:
        for item in results:
            print(item[0], item[1])
    # Catch error if args[1] does not exist.
    else:
        print('Number {} not found.'.format(args[1]))

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
