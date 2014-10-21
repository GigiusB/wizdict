wizdict
=======

Utility library for handling Python dictionaries

## Example Usage

    >>> from wizdict import group_dict, analyze_dict_list
    >>> group_dict([{'A': 1, 'B': 2, 'C': 3}, {'A': 1, 'C': 33}, {'A': 22, 'B': 2, 'C': None}], 'A')
    {1: [{'A': 1, 'B': 2, 'C': 3}, {'A': 1, 'C': 33}], 22: [{'A': 22, 'B': 2, 'C': None}]}

    >>> group_dict([{'A': 1, 'B': 2, 'C': 3}, {'A': 1, 'C': 33}, {'A': 22, 'B': 2, 'C': None}],
        lambda d: 0 if not ('B' in d) else d['B'])
    {0: [{'A': 1, 'C': 33}], 2: [{'A': 1, 'B': 2, 'C': 3}, {'A': 22, 'B': 2, 'C': None}]}

    >>> analyze_dict_list([{'A': 1, 'B': 2, 'C': 3}, {'A': 1, 'C': 33}, {'A': 22, 'B': 2, 'C': None}],
         ['A', '-C'])
    {'C_min': 33, 'C_max': 3, 'C_cnt': 2, 'C_sum': 36, 'C_avg': 18.0, 'C_med': 33,
       'A_min': 1, 'A_max': 22, 'A_cnt': 3, 'A_sum': 24, 'A_avg': 8.0, 'A_med': 22 }