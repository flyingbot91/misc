#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Palindromes
"""

__author__ = "flyingbot91"
__copyright__ = "Copyright 2019"
__date__ = "2019/11/07"
__credits__ = ["flyingbot91"]
__license__ = " GPLv3"
__version__ = "0.0.1"
__maintainer__ = "flyingbot91"
__status__ = "Development"


def palindrome_1(orig_str):
    """
    Check whether <orig_str> is a palindrome or not.
    :param orig_str: (str)
    :return: (bool)
    """

    orig_str = orig_str.casefold()
    rev_str = reversed(orig_str)

    return list(orig_str) == list(rev_str)


def palindrome_2(orig_str):
    """
    Check whether <orig_str> is a palindrome or not.
    :param orig_str: (str)
    :return: (bool)
    """

    return orig_str == orig_str[::-1]
