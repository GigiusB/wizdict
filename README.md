wizdict
=======

Utility library for handling Python dictionaries

## Example Usage

    >>> from wizdict import group_dict
    >>> group_dict([{'A': 1, 'B': 2, 'C': 3}, {'A': 1, 'C': 33}, {'A': 22, 'B': 2, 'C': None}], 'A')
    {1: [{'A': 1, 'B': 2, 'C': 3}, {'A': 1, 'C': 33}], 22: [{'A': 22, 'B': 2, 'C': None}]}