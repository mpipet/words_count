Word count
=============

A simple script to count words from stdin, using only python build in functions
Words with the highest occurence are displayed first.


Requirements
------------

This script is intended to run with Python 2

Installation
------------

``` bash
$ git clone https://github.com/mpipet/words_count.git
```

Usage
----------

``` bash
$ cd words_count
$ echo "foo bar baz foo" | ./words_count.py
2 foo
1 bar
1 baz
```

The script is also provided with an utils module (see utils.py docstring for more infos)
