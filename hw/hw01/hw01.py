
import pandas as pd
import numpy as np


# ---------------------------------------------------------------------
# Question # 0
# ---------------------------------------------------------------------

def consecutive_ints(ints):
    """
    consecutive_ints tests whether a list contains two 
    adjacent elements that are consecutive integers.

    :param ints: a list of integers
    :returns: a boolean value if ints contains two 
    adjacent elements that are consecutive integers.

    :Example:
    >>> consecutive_ints([5,3,6,4,9,8])
    True
    >>> consecutive_ints([1,3,5,7,9])
    False
    """

    if len(ints) == 0:
        return False

    for k in range(len(ints) - 1):
        diff = abs(ints[k] - ints[k+1])
        if diff == 1:
            return True

    return False


# ---------------------------------------------------------------------
# Question # 1 
# ---------------------------------------------------------------------

def median(nums):
    """
    median takes a non-empty list of numbers, 
    returning the median element of the list. 
    If the list has even length, it should return
    the mean of the two elements in the middle.

    :param nums: a non-empty list of numbers.
    :returns: the median of the list.
    
    :Example:
    >>> median([6, 5, 4, 3, 2]) == 4
    True
    >>> m = median([50, 20, 15, 40]) == 30
    True
    """

    return ...

# ---------------------------------------------------------------------
# Question # 2 
# ---------------------------------------------------------------------

def lcm3(a, b, c):
    """
    lcm3 returns the least common multiple of a,b,c.

    :param a: a positive integer
    :param b: a positive integer
    :param c: a positive integer
    :returns: the LCM of a,b,c.

    :Example:
    >>> lcm3(1,2,3)
    6
    >>> lcm3(4,6,12)
    12
    """

    return ...

# ---------------------------------------------------------------------
# Question # 3 
# ---------------------------------------------------------------------

def same_diff_ints(ints):
    """
    same_diff_ints tests whether a list contains
    two list elements i places apart, whose distance 
    as integers is also i.

    :param ints: a list of integers
    :returns: a boolean value if ints contains two 
    elements as described above.

    :Example:
    >>> same_diff_ints([5,3,1,5,9,8])
    True
    >>> same_diff_ints([1,3,5,7,9])
    False
    """

    return ...

# ---------------------------------------------------------------------
# Question # 4 
# ---------------------------------------------------------------------

def prefixes(s):
    """
    prefixes returns a string of every 
    consecutive prefix of the input string.

    :param s: a string.
    :returns: a string of every consecutive prefix of s.

    :Example:
    >>> prefixes('Data!')
    'DDaDatDataData!'
    >>> prefixes('Marina')
    'MMaMarMariMarinMarina'
    >>> prefixes('aaron')
    'aaaaaraaroaaron'
    """

    return ...

# ---------------------------------------------------------------------
# Question # 5 
# ---------------------------------------------------------------------

def evens_reversed(N):
    """
    evens_reversed returns a string containing 
    all even integers from  1  to  N  (inclusive)
    in reversed order, separated by spaces. 
    Each integer is zero padded.

    :param N: a non-negative integer.
    :returns: a string containing all even integers 
    from 1 to N reversed, formatted as decsribed above.

    :Example:
    >>> evens_reversed(7)
    '6 4 2'
    >>> evens_reversed(10)
    '10 08 06 04 02'
    """
    
    return ...

# ---------------------------------------------------------------------
# Question # 6 
# ---------------------------------------------------------------------

def last_chars(fh):
    """
    last_chars takes a file object and returns a 
    string consisting of the last character of the line.

    :param fh: a file object to read from.
    :returns: a string of last characters from fh

    :Example:
    >>> last_chars(open('chars.txt'))
    hrg
    """

    return ...



# ---------------------------------------------------------------------
# Question # 7 
# ---------------------------------------------------------------------

def cnt_values(s):
    """
    cnt_values returns counts of all two 
    character combinations in string s.

    :param s: a string.
    :returns: a dictionary whose:
    - keys are two character combinations, lower-case, 
    and only part of words.
    - values are counts of each two character combination.

    :Example:
    >>> s = 'In linen, moment'
    >>> cnt_values(s)
    {'in': 2, 'li': 1, 'ne': 1, 'en': 2, 'mo': 1, 'om': 1, 'me': 1, 'nt': 1}
    """

    return ...


def list_cnts(d):
    """
    list_cnts takes in a dictionary, as described above,
    and returns a list of the top 5 most common 
    letter combinations in descending order.

    :param d: a dictionary of counts as returned by cnt_values.
    :returns: a list of the top 5 most common letter
    combinations in descending order.

    :Example:
    >>> s = 'In linen, moment'
    >>> list_cnts(cnt_values(s))
    ['in', 'en', 'li', 'ne', 'mo']
    """

    return ...



# ---------------------------------------------------------------------
# Question # 8
# ---------------------------------------------------------------------

def airport_arrival_stats(aircode):
    """
    airport_arrival_stats that takes in an airport 
    code `aircode` and outputs a list with the 
    following quantities, in the following order:
    - number of arriving flights to `aircode`.
    - average flight delay of arriving flights to `aircode`.
    - median flight delay of arriving flights to `aircode`.
    - the airline code of the airline that most often 
    arrives to `aircode`.
    - the proportion of arriving flights to `aircode` that 
    are cancelled in July 2015.
    - the airline code of the airline with the longest flight 
    delay among all flights arriving to `aircode`.

    :param aircode: a string signifying an airport code.
    :returns: a list of stats as described above.

    :Example:
    >>> isinstance(airport_arrival_stats('SAN'), list)
    True
    """

    return ...

# ---------------------------------------------------------------------
# Question # 9 
# ---------------------------------------------------------------------

def late_airlines(aircode):
    """
    late_airlines that takes in an airport code 
    `aircode` and returns a Series, indexed by airline, 
    that contains the proportion of each airline's 
    flights that departed at least two standard 
    deviatins above the mean departure delay 
    (of flights leaving or arriving `aircode`).

    :param aircode: a string signifying airport code.
    :returns: a pd.Series index by airline as described above.

    :Example:
    >>> san = late_airlines('SAN')
    >>> isinstance(san, pd.Series)
    True
    >>> (san < 1).all() and (san > 0).all()
    True
    >>> 'UA' in san.index
    True
    """

    return ...


def all_late_flights(aircode):
    """
    all_late_flights returns a dataframe of all flights either 
    leaving or arriving `aircode` that departed at least two standard 
    deviatins above the mean departure delay (of all flights 
    leaving or arriving `aircode`).

    :param aircode: a string signifying airport code.
    :returns: a pd.DataFrame of flights as described above.

    :Example:
    >>> san = all_late_flights('SAN')
    >>> isinstance(san, pd.DataFrame)
    True
    >>> 'AIRLINE' in san.columns
    True
    """

    return ...


# ---------------------------------------------------------------------
# Question # 10
# ---------------------------------------------------------------------

def cancel_cnt_airport(fh):
    """
    returns the number of cancelled flights for 
    each airport using out-of-memory techniques 
    (chunking; chunk-size=1000).

    :param fh: an open file object of a csv-file like `flights.csv`.
    :returns: a pd.Series, indexed by airport, of the 
    number of cancelled flights for each airport.

    :Example:
    >>> cancels = cancel_cnt_airport(open('flights.csv'))
    >>> isinstance(cancels, pd.Series)
    """

    return ...



# ---------------------------------------------------------------------
# DO NOT TOUCH BELOW THIS LINE
# IT'S FOR YOUR OWN BENEFIT!
# ---------------------------------------------------------------------


# Graded functions names! DO NOT CHANGE!
# This dictionary provides your doctests with
# a check that all of the questions being graded
# exist in your code!

GRADED_FUNCTIONS = {
    'q00': ['consecutive_ints'],
    'q01': ['median'],
    'q02': ['lcm3'],
    'q03': ['same_diff_ints'],
    'q04': ['prefixes'],
    'q05': ['evens_reversed'],
    'q06': ['last_chars'],
    'q07': ['cnt_values', 'list_cnts'],
    'q08': ['airport_arrival_stats'],
    'q09': ['late_airlines', 'all_late_flights'],
    'q10': ['cancel_cnt_airport']
}


def check_for_graded_elements():
    """
    >>> check_for_graded_elements()
    True
    """
    
    for q, elts in GRADED_FUNCTIONS.items():
        for elt in elts:
            if elt not in globals():
                stmt = "YOU CHANGED A QUESTION THAT SHOULDN'T CHANGE! \
                In %s, part %s is missing" %(q, elt)
                raise Exception(stmt)

    return True
