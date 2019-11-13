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

from unittest import TestCase
from algorithms.palindrome import *


class TestCasePalindrome(TestCase):

    dummy = "this is a si siht"

    def test_palindrome_1(self):
        """palindrome_1"""
        self.assertTrue(palindrome_1(self.dummy))

    def test_palindrome_2(self):
        """palindrome_2"""
        self.assertTrue(palindrome_2(self.dummy))

