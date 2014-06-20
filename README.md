## Phonebook

Construct a command-line phonebook tool; timed exercise. This was the result of a timed exercise at [Hacker School](http://hackerschool.com); the spec is posted [here](https://hackpad.com/Manage-those-phone-books-wK1MycZ5ATb) and the version submitted within the timed window is tagged [as_submitted](https://github.com/brannerchinese/phonebook/tree/as_submitted).

### To install and use

Clone and run with Python 3. This program uses SQLite3 on the back end.

At the command line:

```
# Create database.
./phonebook.py create hsphonebook.pb

# Create unique entry "name" with number 99999.
./phonebook.py add 'name' '99999'

# Look up names containing 'name' as substring and return 
# all entries found.
./phonebook.py lookup 'name'

# Change the number associated with an existing name.
./phonebook.py change 'name' '3456'

# Delete an entry.
./phonebook.py remove 'name'

# Look up names matching 'number' as substring.
./phonebook.py reverse '34'
./phonebook.py reverse-lookup '34'

```

The database name can be supplied after any other arguments, but in its absence, `hsphonebook.pb` is assumed to be the database.

### Old versions (stored in `old_version` to document progress)

 1. `phonebook_as_submitted.py`: Version as actually submitted after two hours' work.
 1. `phonebook_01.py`: Initial version: skeleton code, functions exist and report when they are called.
 1. `phonebook_02.py`: `create` working correctly and reports on creation.
 1. `phonebook_03.py`: `add` working correctly; reports on adding name or on duplicate name.
 1. `phonebook_04.py`: `lookup` (simple) working correctly; reports all found names (including any substring) or on name not found.
 1. `phonebook_05.py`: `reverse` working correctly; reports all found numbers (including any substring) or on number not found.
 1. `phonebook_06.py`: `change` working correctly; makes change and then calls `lookup` on name — this conveniently lets us know if name was not found, though substring results from `lookup`.

### To do

 1. Default argument to `lookup` allow control of substring search - for use when calling `lookup` from within `change` we don't want substring search.
 1. Normalize data.
 1. Test suite.


[end]
