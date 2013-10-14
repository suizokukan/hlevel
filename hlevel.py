#!/usr/bin/python3
# -*- coding: utf-8 -*-
################################################################################
#    HLevel Copyright (C) 2012 Suizokukan
#    Contact: suizokukan _A.T._ orange dot fr
#
#    This file is part of HLevel.
#    HLevel is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    HLevel is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with HLevel.  If not, see <http://www.gnu.org/licenses/>.
################################################################################
"""
    ❏HLevel❏ : hlevel/hlevel.py

    * HLevel class

    formatstring =   "." (separator : one character)
                   + "(" (prefix : zero, one or more characters)
                   + "A.I.3" (symbols followed by the separator, if the separator is a non empty
                              string). Available symbols : see HLevel.reprnum
                   + ")" (suffix : zero, one or more characters)

    If you want the first number to be <n>, set self.first_number to <n>; by example, with
    self.first_number set to 0, the first number will be 0 (and not 1).
"""

################################################################################
class HLevel(list):
    """
        HLevel class
    """

    # default representation of the object :
    defaultformat = ".(1111111111)"

    # accepted symbols in a format string :
    reprnum = [ "1", "I", "i", "A", "a", "①", "一", "¹", "₁", "１" ]

    forbidden_characters_in_prefix_and_suffix = [
                "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
                
                "a", "b", "c", "d", "e", "f", "g", "h", "i",
                "j", "k", "l", "m", "n", "o", "p", "q", "r",
                "s", "t", "u", "v", "w", "x", "y", "z",

                "A", "B", "C", "D", "E", "F", "G", "H", "I",
                "J", "K", "L", "M", "N", "O", "P", "Q", "R",
                "S", "T", "U", "V", "W", "X", "Y", "Z",

                "①", "②", "③", "④", "⑤",
                "⑥", "⑦", "⑧", "⑨", "⑩",
                "⑪", "⑫", "⑬", "⑭", "⑮",
                "⑯", "⑰", "⑱", "⑲", "⑳",

                '〇', '一', '二', '三', '四', '五', '六', '七', '八', '九',
                '十', '百', '千',

                '⁰', '¹', '²', '³', '⁴', '⁵', '⁶', '⁷', '⁸', '⁹',

                '₀', '₁', '₂', '₃', '₄', '₅', '₆', '₇', '₈', '₉',

                "０", "１", "２", "３", "４", "５", "６", "７", "８", "９",
                ]

    arabicnumber_symbols = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9",)

    capitalletter_symbols = ("A", "B", "C", "D", "E", "F", "G", "H", "I", \
                             "J", "K", "L", "M", "N", "O", "P", "Q", "R", \
                             "S", "T", "U", "V", "W", "X", "Y", "Z",)

    lowercaseletter_symbols = ("a", "b", "c", "d", "e", "f", "h", "j", "i", \
                             "j", "k", "l", "m", "n", "o", "p", "q", "r", \
                             "s", "t", "u", "v", "w", "x", "y", "z",)

    capitalromannumber_symbols = ( "I", "V", "X", "L", "C", "D", "M" )

    lowercaseromannumber_symbols = ( "i", "v", "x", "l", "c", "d", "m" )

    enclosedletter_symbols = ( "①", "②", "③", "④", "⑤",
                               "⑥", "⑦", "⑧", "⑨", "⑩",
                               "⑪", "⑫", "⑬", "⑭", "⑮",
                               "⑯", "⑰", "⑱", "⑲", "⑳" )

    #///////////////////////////////////////////////////////////////////////////
    def __init__(self, src=None, formatstr=None, first_number = 1):
        """
                HLevel.__init__

                src             : (str)
                formatstr       :  str or None
                first_number    : (int)

                about <first_number> :
                Beware ! The normal value for <first_number> is 1 : 'A'=1, 'B'=2, ..., "AA" = 27,
                ... Use other values only if you know exactly what your doing; by example, with
                <first_number> set to 0, 'A'=0, 'AA'=0, 'B'=1, 'AB' = 'B' = 1, ...
                Some number representations demand that <first_number> be set to 1 : capital roman
                number, lowletter roman number and enclosed number.
        """
        list.__init__(self)

        self.first_number = first_number

        if formatstr is None:
            self.setFormat( HLevel.defaultformat )
        else:
            self.setFormat( formatstr )

        if src is not None:
            self.initFromStr(src)

    #///////////////////////////////////////////////////////////////////////////
    def getNumberFromArabicNumber( self, strnumber ):
        """
                HLevel.getNumberFromArabicNumber

                strnumber       : (str)
        """
        if len( [char for char in strnumber if char not in HLevel.arabicnumber_symbols]) != 0:
            msg = "(HLevel.getNumberFromArabicNumber) " \
                  "In '{0}', there is (at least) one unknown symbol. " \
                  "Allowed symbols are {1}."
            raise Exception(msg.format(strnumber,
                                       HLevel.arabicnumber_symbols))
                    
        return int(strnumber)

    #///////////////////////////////////////////////////////////////////////////
    def getNumberFromCapitalLetter( self, strnumber ):
        """
                HLevel.getNumberFromCapitalLetter

                strnumber       : (str)
        """
        if len( [char for char in strnumber if char not in HLevel.capitalletter_symbols]) != 0:
            msg = "(HLevel.getNumberFromCapitalLetter) " \
                  "In '{0}', there is (at least) one unknown symbol. " \
                  "Allowed symbols are {1}."
            raise Exception(msg.format(strnumber,
                                       HLevel.capitalletter_symbols))

        res = 0
        for index_char, char in enumerate(strnumber[::-1]):
            res += (26 ** index_char) * (ord(char) - 65 + self.first_number)
            
        return res

    #///////////////////////////////////////////////////////////////////////////
    def getNumberFromCapitalRomanNumber( self, strnumber ):
        """
                HLevel.getNumberFromCapitalRomanNumber

                strnumber       : (str)
        """
        if len( [char for char in strnumber if char not in HLevel.capitalromannumber_symbols]) != 0:
            msg = "(HLevel.getNumberFromCapitalRomanNumber) " \
                  "In '{0}', there is (at least) one unknown symbol. " \
                  "Allowed symbols are {1}."
            raise Exception(msg.format(strnumber,
                                       HLevel.capitalromannumber_symbols))

        if self.first_number != 1:
            msg = "(HLevel.getNumberFromCapitalRomanNumber) " \
                  "You can't use roman numbers (number read : {0}) if " \
                  "self.first_number (='{0}') is not set to 1."
            raise Exception(msg.format(strnumber,
                                       self.first_number))

        data = (('M',  1000),
                ('CM', 900),
                ('D',  500),
                ('CD', 400),
                ('C',  100),
                ('XC', 90),
                ('L',  50),
                ('XL', 40),
                ('X',  10),
                ('IX', 9),
                ('V',  5),
                ('IV', 4),
                ('I',  1))

        res = 0
        index = 0
        for numeral, integer in data:
            while strnumber[index:index+len(numeral)] == numeral:
                res += integer
                index += len(numeral)
                
        return res

    #///////////////////////////////////////////////////////////////////////////
    def getNumberFromEnclosedNumber( self, strnumber ):
        """
                HLevel.getNumberFromEnclosedNumber

                strnumber       : (str)                
        """
        if len( [char for char in strnumber if char not in HLevel.enclosedletter_symbols]) != 0:
            msg = "(HLevel.getNumberFromEnclosedNumber) " \
                  "In '{0}', there is (at least) one unknown symbol. " \
                  "Allowed symbols are {1}."
            raise Exception(msg.format(strnumber,
                                       HLevel.enclosedletter_symbols))

        if len(strnumber) != 1:
            msg = "(HLevel.getNumberFromEnclosedNumber) " \
                  "Multiple character in '{0}', which is forbidden."
            raise Exception(msg.format(strnumber))

        return ord(strnumber) - 0x2460 + 1

    #///////////////////////////////////////////////////////////////////////////
    def getNumberFromLowercaseLetter( self, strnumber ):
        """
                HLevel.getNumberFromLowercaseLetter

                strnumber       : (str)
        """
        if len( [char for char in strnumber if char not in HLevel.lowercaseletter_symbols]) != 0:
            msg = "(HLevel.getNumberFromLowercaseLetter) " \
                  "In '{0}', there is (at least) one unknown symbol. " \
                  "Allowed symbols are {1}."
            raise Exception(msg.format(strnumber,
                                       HLevel.lowercaseletter_symbols))

        res = 0
        for index_char, char in enumerate(strnumber[::-1]):
            res += (26 ** index_char) * (ord(char) - 97 + self.first_number)
            
        return res

    #///////////////////////////////////////////////////////////////////////////
    def getNumberFromLowercaseRomanNumber( self, strnumber ):
        """
                HLevel.getNumberFromLowercaseRomanNumber

                strnumber       : (str)
        """
        if len( [char for char in strnumber if char not in HLevel.lowercaseromannumber_symbols]) != 0:
            msg = "(HLevel.getNumberFromLowercaseRomanNumber) " \
                  "In '{0}', there is (at least) one unknown symbol. " \
                  "Allowed symbols are {1}."
            raise Exception(msg.format(strnumber,
                                       HLevel.lowercaseromannumber_symbols))

        if self.first_number != 1:
            msg = "(HLevel.getNumberFromLowercaseRomanNumber) " \
                  "You can't use roman numbers (number read : {0}) if " \
                  "self.first_number (='{0}') is not set to 1."
            raise Exception(msg.format(strnumber,
                                       self.first_number))

        return self.getNumberFromCapitalRomanNumber( strnumber.upper() )

    #///////////////////////////////////////////////////////////////////////////
    def getRepr(self):
        """
                HLevel.getRepr
        """
        res = []

        # prefix :
        res.append( self.prefix )

        len_self = len(self)
        len_numbers_format = len(self.numbers_format)

        # numbers :
        for number_index, number in enumerate(self):

            if number < self.first_number:
                msg = "(HLevel.getRepr) number {0} is less than self.first_number={1}"
                raise Exception(msg.format(number,
                                           self.first_number))

            if number_index+1 > len_numbers_format:
                msg = "HLevel.getRepr : too many numbers in {0}; expected pattern is {1}."
                raise Exception( msg.format(".".join( map(str, self)),
                                              self.numbers_format))

            number_format = self.numbers_format[number_index]

            if number_format == '1':
                res.append( self.getReprArabicNumber( number ))

            elif number_format == 'A':
                res.append( self.getReprCapitalLetter( number ))

            elif number_format == 'a':
                res.append( self.getReprLowerCaseLetter( number ))

            elif number_format == 'I':
                res.append( self.getReprCapitalRomanNumber( number ))

            elif number_format == 'i':
                res.append( self.getReprLowerCaseRomanNumber( number ))

            elif number_format == '①':
                res.append( self.getReprEnclosedNumber( number ))

            elif number_format == '一':
                res.append( self.getReprJapaneseNumber( number ))

            elif number_format == '¹':
                res.append( self.getReprSuperscriptNumeral( number ))

            elif number_format == '₁':
                res.append( self.getReprSubscriptNumeral( number ))

            elif number_format == '１':
                res.append( self.getReprArabicNumberFullWidth( number ))
                
            else:
                msg = "HLevel.getRepr : unknown number format '0'; expected formats are {1}."
                raise Exception(msg.format(number_format,
                                             HLevel.reprnum))

            # separator ?
            if number_index+1 < len_self:
                res.append( self.separator )

        # suffix :
        res.append( self.suffix )

        # return value :
        return "".join(res)

    #///////////////////////////////////////////////////////////////////////////
    def getReprArabicNumber(self, number):
        """
                HLevel.getReprArabicNumber

                number  : (int)
        """
        return str(number)

    #///////////////////////////////////////////////////////////////////////////
    def getReprArabicNumberFullWidth(self, number):
        """
                HLevel.getReprArabicNumberFullWidth

                number  : (int)
        """
        strnumber = str(number)

        res = []

        digit_to_fullwidthdigit = {
                "-"     : "-",
                "0"     : "０",
                "1"     : "１",
                "2"     : "２",
                "3"     : "３",
                "4"     : "４",
                "5"     : "５",
                "6"     : "６",
                "7"     : "７",
                "8"     : "８",
                "9"     : "９",
            }

        for digit in str(number):
            res.append( digit_to_fullwidthdigit[digit] )

        return "".join(res)

    #///////////////////////////////////////////////////////////////////////////
    def getReprCapitalLetter(self, number):
        """
                HLevel.getReprCapitalLetter

                number  : (int)
        """
        return self.stringBase( number = number,
                                base = 26,
                                digits = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" )

    #///////////////////////////////////////////////////////////////////////////
    def getReprCapitalRomanNumber(self, number):
        """
                HLevel.getReprCapitalRomanNumber

                number  : (int)
        """
        if number < 0:
            msg = "HLevel.getReprCapitalRomanNumber : can interpret number {0} as " \
                  "a Roman numeral. Number must be greater than 0."
            raise Exception( msg.format(number) )

        if self.first_number != 1:
            msg = "(HLevel.getReprCapitalRomanNumber) " \
                  "You can't use roman numbers (number read : {0}) if " \
                  "self.first_number (='{0}') is not set to 1."
            raise Exception(msg.format(number,
                                       self.first_number))
        
        data = (('M',  1000),
                ('CM', 900),
                ('D',  500),
                ('CD', 400),
                ('C',  100),
                ('XC', 90),
                ('L',  50),
                ('XL', 40),
                ('X',  10),
                ('IX', 9),
                ('V',  5),
                ('IV', 4),
                ('I',  1))

        res = ""
        n = number
        
        for num, integer in data:
            while n >= integer:
                res += num
                n -= integer
                
        return res

    #///////////////////////////////////////////////////////////////////////////
    def getReprEnclosedNumber(self, number):
        """
                HLevel.getReprEnclosedNumber

                number  : (int)
        """
        if number < 1 or number > 20:
            msg = "HLevel.getReprEnclosedNumber : can interpret number {0} as " \
                  "an enclosed numeral. Expected range is [1;20]"
            raise Exception( msg.format(number) )

        if self.first_number != 1:
            msg = "(HLevel.getReprEnclosedNumber) " \
                  "You can't use enclosed numbers (number read : {0}) if " \
                  "self.first_number (='{0}') is not set to 1."
            raise Exception(msg.format(number,
                                       self.first_number))

        return chr(0x2460 + number - 1 )

    #///////////////////////////////////////////////////////////////////////////
    def getReprJapaneseNumber(self, number):
        """
                HLevel.getReprJapaneseNumber

                number  : (int)
        """
        if number < 1 or number > 9999:
            msg = "HLevel.getReprJapaneseNumber : can interpret number {0} as " \
                  "a Japanese number. Expected range is [1;9999]"
            raise Exception( msg.format(number) )

        japanese_digits = [ '〇', '一', '二', '三', '四', '五', '六', '七', '八', '九']

        res = []
        strnumber = str(number)

        for position, digit in enumerate(strnumber[::-1]):

            if position == 0:
                res.insert( 0, japanese_digits[int(digit)] )

            elif position == 1 and int(digit) != 0:

                res.insert( 0, "十" )

                if int(digit)>1:
                    res.insert( 0, japanese_digits[int(digit)] )

            elif position == 2 and int(digit) != 0:

                res.insert( 0, "百" )

                if int(digit)>1:
                    res.insert( 0, japanese_digits[int(digit)] )

            elif position == 3 and int(digit) != 0:

                res.insert( 0, "千" )

                if int(digit)>1:
                    res.insert( 0, japanese_digits[int(digit)] )

            else:
                msg = "HLevel.getReprJapaneseNumber : can interpret number {0} as a Japanese number."
                raise Exception( msg.format(number) )
                
        return "".join(res)
    
    #///////////////////////////////////////////////////////////////////////////
    def getReprLowerCaseLetter(self, number):
        """
                HLevel.getReprLowerCaseLetter

                number  : (int)
        """
        return self.stringBase( number = number,
                                base = 26,
                                digits = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" ).lower()

    #///////////////////////////////////////////////////////////////////////////
    def getReprLowerCaseRomanNumber(self, number):
        """
                HLevel.getReprLowerCaseRomanNumber

                number  : (int)
        """
        if number < 0:
            msg = "HLevel.getReprLowercaseRomanNumber : can interpret number {0} as " \
                  "a Roman numeral. Number must be greater than 0."
            raise Exception( msg.format(number) )

        if self.first_number != 1:
            msg = "(HLevel.getReprLowercaseRomanNumber) " \
                  "You can't use roman numbers (number read : {0}) if " \
                  "self.first_number (='{0}') is not set to 1."
            raise Exception(msg.format(number,
                                       self.first_number))

        return self.getReprCapitalRomanNumber(number).lower()

    #///////////////////////////////////////////////////////////////////////////
    def getReprSubscriptNumeral(self, number):
        """
                HLevel.getReprSubscriptNumeral

                number  : (int)
        """
        strnumber = str(number)

        res = []

        digit_to_subscriptdigit = {
                "-"     : "-",
                "0"     : chr(0x2080),
                "1"     : chr(0x2081),
                "2"     : chr(0x2082),
                "3"     : chr(0x2083),
                "4"     : chr(0x2084),
                "5"     : chr(0x2085),
                "6"     : chr(0x2086),
                "7"     : chr(0x2087),
                "8"     : chr(0x2088),
                "9"     : chr(0x2089),
            }

        for digit in str(number):
            res.append( digit_to_subscriptdigit[digit] )

        return "".join(res)

    #///////////////////////////////////////////////////////////////////////////
    def getReprSuperscriptNumeral(self, number):
        """
                HLevel.getReprSuperscriptNumeral

                number  : (int)
        """
        strnumber = str(number)

        res = []

        digit_to_superscriptdigit = {
                "-"     : "-",
                "0"     : chr(0x2070),
                "1"     : chr(0x00B9),
                "2"     : chr(0x00B2),
                "3"     : chr(0x00B3),
                "4"     : chr(0x2074),
                "5"     : chr(0x2075),
                "6"     : chr(0x2076),
                "7"     : chr(0x2077),
                "8"     : chr(0x2078),
                "9"     : chr(0x2079),
            }

        for digit in str(number):
            res.append( digit_to_superscriptdigit[digit] )

        return "".join(res)

    #///////////////////////////////////////////////////////////////////////////
    def initFromStr(self, _src):
        """
                HLevel.initFromStr

                _src     : (str)

                Initialize <self> from (str)_src.
        """
        if not (_src.startswith(self.prefix) and _src.endswith(self.suffix)):

            msg = "(HLevel.initFromStr) missing prefix '{0}' or suffix '{1}' in string '{2}'."
            raise Exception(msg.format(self.prefix,
                                       self.suffix,
                                       _src))

        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        self.clear()

        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # no prefix, no suffix :
        src = _src[len(self.prefix):-len(self.suffix)]

        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        for strnumber_index, strnumber in enumerate(src.split(self.separator)):

            number_format = self.numbers_format[strnumber_index]

            if number_format == '1':
                self.append( self.getNumberFromArabicNumber( strnumber ))

            elif number_format == 'A':
                self.append( self.getNumberFromCapitalLetter( strnumber ))

            elif number_format == 'a':
                self.append( self.getNumberFromLowercaseLetter( strnumber ))

            elif number_format == 'I':
                self.append( self.getNumberFromCapitalRomanNumber( strnumber ))

            elif number_format == 'i':
                self.append( self.getNumberFromLowercaseRomanNumber( strnumber ))

            elif number_format == '①':
                self.append( self.getNumberFromEnclosedNumber( strnumber ))

    #///////////////////////////////////////////////////////////////////////////
    def setFormat(self, formatstr):
        """
                HLevel.setFormat

                src     : (str)
        """
        if len(formatstr) == 0:
            raise Exception( "HLevel.setFormat : empty format string" )

        self.separator = ""
        self.prefix = ""
        self.suffix = ""
        self.numbers_format = []

        for index_char, char in enumerate(formatstr):

            if index_char == 0:
                self.separator = char

            elif char == self.separator:
                pass

            elif char not in HLevel.reprnum and len(self.numbers_format) == 0:
                self.prefix += char

            elif char in HLevel.reprnum:
                self.numbers_format.append(char)

            elif char not in HLevel.forbidden_characters_in_prefix_and_suffix:
                self.suffix += char

            else:
                raise Exception("HLevel.setFormat : wrong format string = '{0}'".format(formatstr))

    #///////////////////////////////////////////////////////////////////////////
    def stringBase(self,
                   number,
                   base,
                   digits = "0123456789ABCDEF"):
        """
                   HLevel.stringBase

                   number       : (int)
                   base         : (int)
                   digits       : (str)symbols like "01234564789"

                   Return the string corresponding to <number> written in the base <base> using
                   the <digits>.
        """
        (d, m) = divmod(number - self.first_number, base)
        if d:
            return self.stringBase(d, base, digits) + digits[m]
        else:
            return digits[m]
