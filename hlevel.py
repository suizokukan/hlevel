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
                   + "(" (prefix : zero, one or several characters)
                   + "A.I.3" (symbols followed by the separator, if the separator is a non empty
                              string). Available symbols : see HLevel.reprnum
                   + ")" (suffix : zero, one or several characters)

    If you want the first number to be <n>, set self.first_number to <n>; by example, with
    self.first_number set to 0, the first number will be 0 (and not 1).


    How it works :
        hl = HLevel( src="(C.IX.3)", formatstr = ".(A.I.1.α)" )
        hl.append(4)
        print(hl)               # (C.IX.3.δ)

        hl1 = HLevel( src="(C.IX.3)", formatstr = ".(A.I.1.α)" )
        hl2 = HLevel( src="{8.7}", formatstr = ".{1.1}" )
        print(hl1 < hl2)        # True

    Known formats :
    * Arabic numbers ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10" ...)
      negative, null or positive integers
      
    * capital letters ("A", "B", "C", "D", "E", ..., "X", "Y", "Z", "AZ", ...)
      positive integers, normally greater than zero (but see self.first_number)
    
    * lower case letters ("a", "b", "c", "d", "e", ..., "x", "y", "z" "az", ...)
      positive integers, normally greater than zero (but see self.first_number)
    
    * capital roman numbers ("I", "II", "III", ... "X", "XI", ... "MDCCCLIX", ...)
      positive integers, normally greater than zero (but see self.first_number)
    
    * lower case roman numbers ("i", "ii", "iii", ... "x", "xi", ... "mdccclix", ...)
      positive integers, normally greater than zero (but see self.first_number)
    
    * enclosed letters ( "①", "②", "③", "④", "⑤", ... "⑯", "⑰", "⑱", "⑲", "⑳" )
      only 20 numbers available (from 1 to 20)
      
    * Japanese numbers ( '〇', '一', '二', '三', ..., '九', "十", "十一", ... "百", ... "千", ... )
      null ('〇') or positive integers
    
    * superscript_symbols ("⁰", "¹", "²", "³", "⁴", "⁵", "⁶", "⁷", "⁸", "⁹", "¹⁰", ...)
      negative, null or positive integers

    * subscript_symbols ("₀", "₁", "₂", "₃", "₄", "₅", "₆", "₇", "₈", "₉", "₁₀", ...)
      negative, null or positive integers

    * fullwidthnumerals_symbols = ("０", "１", "２", "３", "４", "５", "６", "７", "８", "９", "１０", ...)
      negative, null or positive integers

    * lowercasegreek_symbols = ( "α", "β", "γ", "δ", "ε", "ζ", ..., "χ", "ψ", "ω", "αα", ... )
      positive integers, normally greater than zero (but see self.first_number)

    * capitalgreek_symbols = ( "Α", "Β", "Γ", "Δ", "Ε", "Ζ", ..., "Φ", "Χ", "Ψ", "Ω", "ΑΑ", ... )
      positive integers, normally greater than zero (but see self.first_number)    
"""

import re

################################################################################
class HLevel(list):
    """
        HLevel class
    """

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # default representation of the object :
    defaultformat = ".(1111111111)"

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # accepted symbols in each format string :
    reprnum = [ "1", "I", "i", "A", "a", "①", "一", "¹", "₁", "１", "α", "Α" ]

    arabicnumber_symbols = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9",)

    capitalletter_symbols = ("A", "B", "C", "D", "E", "F", "G", "H", "I", \
                             "J", "K", "L", "M", "N", "O", "P", "Q", "R", \
                             "S", "T", "U", "V", "W", "X", "Y", "Z",)

    lowercaseletter_symbols = ("a", "b", "c", "d", "e", "f", "g", "h", "i", \
                             "j", "k", "l", "m", "n", "o", "p", "q", "r", \
                             "s", "t", "u", "v", "w", "x", "y", "z",)

    capitalromannumber_symbols = ( "I", "V", "X", "L", "C", "D", "M" )

    lowercaseromannumber_symbols = ( "i", "v", "x", "l", "c", "d", "m" )

    enclosedletter_symbols = ( "①", "②", "③", "④", "⑤",
                               "⑥", "⑦", "⑧", "⑨", "⑩",
                               "⑪", "⑫", "⑬", "⑭", "⑮",
                               "⑯", "⑰", "⑱", "⑲", "⑳" )

    japanesenumber_symbols = ( '〇', '一', '二', '三', '四', '五', '六', '七', '八', '九',
                               "十", "百", "千" )

    superscript_symbols = ( "-",
                            chr(0x2070), chr(0x00B9), chr(0x00B2), chr(0x00B3), chr(0x2074),
                            chr(0x2075), chr(0x2076), chr(0x2077), chr(0x2078), chr(0x2079)
                            )

    subscript_symbols = ( "-",
                          chr(0x2080), chr(0x2081), chr(0x2082), chr(0x2083), chr(0x2084),
                          chr(0x2085), chr(0x2086), chr(0x2087), chr(0x2088), chr(0x2089)
                        )

    fullwidthnumerals_symbols = ("０", "１", "２", "３", "４", "５", "６", "７", "８", "９",)

    lowercasegreek_symbols = ( "α", "β", "γ", "δ", "ε", "ζ", "η", "θ",
                               "ι", "κ", "λ", "μ", "ν", "ξ", "ο", "π",
                               "ρ", "σ", "τ", "υ", "φ", "χ", "ψ", "ω" )

    capitalgreek_symbols = ( "Α", "Β", "Γ", "Δ", "Ε", "Ζ", "Η", "Θ",
                             "Ι", "Κ", "Λ", "Μ", "Ν", "Ξ", "Ο", "Π",
                             "Ρ", "Σ", "Τ", "Υ", "Φ", "Χ", "Ψ", "Ω" )

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # forbidden characters in prefix and suffix string :
    invalid_chars_in_pre_suffix = (
                arabicnumber_symbols + \
                capitalletter_symbols + \
                lowercaseletter_symbols + \
                capitalromannumber_symbols + \
                lowercaseromannumber_symbols + \
                enclosedletter_symbols + \
                japanesenumber_symbols + \
                superscript_symbols + \
                subscript_symbols + \
                fullwidthnumerals_symbols + \
                lowercasegreek_symbols + \
                capitalgreek_symbols )

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

        self.separator = ""
        self.prefix = ""
        self.suffix = ""
        self.numbers_format = [] # E.g ['A', 'I', '1']

        self.first_number = first_number

        if formatstr is None:
            self.setFormat( HLevel.defaultformat )
        else:
            self.setFormat( formatstr )

        if src is not None:
            self.initFromStr(src)

    #///////////////////////////////////////////////////////////////////////////
    def __repr__(self):
        """
                HLevel.__repr__
        """
        string = "(HLevel) separator='{0}'; prefix='{1}'; " \
                 "suffix='{2}'; numbers_format='{3}'; data={4}"
        return string.format(self.separator,
                             self.prefix,
                             self.suffix,
                             self.numbers_format,
                             ".".join( str(value) for value in self))

    #///////////////////////////////////////////////////////////////////////////
    def __str__(self):
        """
                HLevel.__str__
        """
        return self.getRepr()

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
    def getNumberFromCapitalGreekLetter( self, strnumber ):
        """
                HLevel.getNumberFromCapitalGreekLetter

                strnumber       : (str)
        """
        if len( [char for char in strnumber if char not in HLevel.capitalgreek_symbols]) != 0:
            msg = "(HLevel.getNumberFromCapitalGreekLetter) " \
                  "In '{0}', there is (at least) one unknown symbol. " \
                  "Allowed symbols are {1}."
            raise Exception(msg.format(strnumber,
                                       HLevel.capitalgreek_symbols))

        res = 0
        for index_char, char in enumerate(strnumber[::-1]):
            res += (24 ** index_char) * (ord(char) - 0x391 + self.first_number)

        return res

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
    def getNumberFromFullWidthNumeral(self, strnumber ):
        """
                HLevel.getNumberFromFullWidthNumeral
        """
        if len( [char for char in strnumber if char not in HLevel.fullwidthnumerals_symbols]) != 0:
            msg = "(HLevel.getNumberFromFullWidthNumeral) " \
                  "In '{0}', there is (at least) one unknown symbol. " \
                  "Allowed symbols are {1}."
            raise Exception(msg.format(strnumber,
                                       HLevel.fullwidthnumerals_symbols))

        data = { "-"    : "-",
                 "０"   : 0,
                 "１"   : 1,
                 "２"   : 2,
                 "３"   : 3,
                 "４"   : 4,
                 "５"   : 5,
                 "６"   : 6,
                 "７"   : 7,
                 "８"   : 8,
                 "９"   : 9}

        _strnumber = "".join( str(data[char]) for char in strnumber )

        return int(_strnumber)

    #///////////////////////////////////////////////////////////////////////////
    def getNumberFromJapaneseNumber( self, strnumber ):
        """
                HLevel.getNumberFromJapaneseNumber

                strnumber       : (str)
        """
        if len( [char for char in strnumber if char not in HLevel.japanesenumber_symbols]) != 0:
            msg = "(HLevel.getNumberFromJapaneseNumber) " \
                  "In '{0}', there is (at least) one unknown symbol. " \
                  "Allowed symbols are {1}."
            raise Exception(msg.format(strnumber,
                                       HLevel.japanesenumber_symbols))

        data_digits = {'一' : 1,
                       '二' : 2,
                       '三' : 3,
                       '四' : 4,
                       '五' : 5,
                       '六' : 6,
                       '七' : 7,
                       '八' : 8,
                       '九' : 9}

        data_mul = {'十' : 10,
                    '百' : 100,
                    '千' : 1000,}

        if strnumber == '〇':
            return 0

        else:
            res = 0
            digit = None
            mul = 0
            for index_char, char in enumerate(strnumber):

                if char in data_mul:
                    mul = data_mul[char]
                    if digit is None:
                        res += mul
                    else:
                        res += mul * digit

                    digit = None
                    mul = 0
                else:
                    digit = data_digits[char]
                    mul = 0

                    if index_char == len(strnumber)-1:
                        res += digit

        return res

    #///////////////////////////////////////////////////////////////////////////
    def getNumberFromLowercGreekLetter( self, strnumber ):
        """
                HLevel.getNumberFromLowercGreekLetter

                strnumber       : (str)
        """
        if len( [char for char in strnumber if char not in HLevel.lowercasegreek_symbols]) != 0:
            msg = "(HLevel.getNumberFromLowercGreekLetter) " \
                  "In '{0}', there is (at least) one unknown symbol. " \
                  "Allowed symbols are {1}."
            raise Exception(msg.format(strnumber,
                                       HLevel.lowercasegreek_symbols))

        res = 0
        for index_char, char in enumerate(strnumber[::-1]):
            res += (24 ** index_char) * (ord(char) - 0x3B1 + self.first_number)

        return res

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
    def getNumberFromLowercRomanNumber( self, strnumber ):
        """
                HLevel.getNumberFromLowercRomanNumber

                strnumber       : (str)
        """
        if len( [char for char in strnumber \
                 if char not in HLevel.lowercaseromannumber_symbols]) != 0:
            msg = "(HLevel.getNumberFromLowercRomanNumber) " \
                  "In '{0}', there is (at least) one unknown symbol. " \
                  "Allowed symbols are {1}."
            raise Exception(msg.format(strnumber,
                                       HLevel.lowercaseromannumber_symbols))

        if self.first_number != 1:
            msg = "(HLevel.getNumberFromLowercRomanNumber) " \
                  "You can't use roman numbers (number read : {0}) if " \
                  "self.first_number (='{0}') is not set to 1."
            raise Exception(msg.format(strnumber,
                                       self.first_number))

        return self.getNumberFromCapitalRomanNumber( strnumber.upper() )

    #///////////////////////////////////////////////////////////////////////////
    def getNumberFromSubscriptNumeral(self, strnumber):
        """
                HLevel.getNumberFromSubscriptNumeral
        """
        if len( [char for char in strnumber if char not in HLevel.subscript_symbols]) != 0:
            msg = "(HLevel.getNumberFromSubscriptNumeral) " \
                  "In '{0}', there is (at least) one unknown symbol. " \
                  "Allowed symbols are {1}."
            raise Exception(msg.format(strnumber,
                                       HLevel.subscript_symbols))

        data = { "-"     : "-",
                 chr(0x2080) : 0,
                 chr(0x2081) : 1,
                 chr(0x2082) : 2,
                 chr(0x2083) : 3,
                 chr(0x2084) : 4,
                 chr(0x2085) : 5,
                 chr(0x2086) : 6,
                 chr(0x2087) : 7,
                 chr(0x2088) : 8,
                 chr(0x2089) : 9}

        _strnumber = "".join( str(data[char]) for char in strnumber )

        return int(_strnumber)

    #///////////////////////////////////////////////////////////////////////////
    def getNumberFromSuperscriptNumeral(self, strnumber):
        """
                HLevel.getNumberFromSuperscriptNumeral
        """
        if len( [char for char in strnumber if char not in HLevel.superscript_symbols]) != 0:
            msg = "(HLevel.getNumberFromSuperscriptNumeral) " \
                  "In '{0}', there is (at least) one unknown symbol. " \
                  "Allowed symbols are {1}."
            raise Exception(msg.format(strnumber,
                                       HLevel.superscript_symbols))

        data = { "-"     : "-",
                 chr(0x2070) : 0,
                 chr(0x00B9) : 1,
                 chr(0x00B2) : 2,
                 chr(0x00B3) : 3,
                 chr(0x2074) : 4,
                 chr(0x2075) : 5,
                 chr(0x2076) : 6,
                 chr(0x2077) : 7,
                 chr(0x2078) : 8,
                 chr(0x2079) : 9}

        _strnumber = "".join( str(data[char]) for char in strnumber )

        return int(_strnumber)

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

            elif number_format == 'α':
                res.append( self.getReprLowercaseGreekLetter( number ))

            elif number_format == 'Α':
                res.append( self.getReprCapitalGreekLetter( number ))

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

        for digit in str(strnumber):
            res.append( digit_to_fullwidthdigit[digit] )

        return "".join(res)

    #///////////////////////////////////////////////////////////////////////////
    def getReprCapitalGreekLetter(self, number):
        """
                HLevel.getReprCapitalGreekLetter

                number  : (int)
        """
        return self.stringBase( number = number,
                                base = 24,
                                digits = "ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ" )

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
        decreasing_num = number

        for num, integer in data:
            while decreasing_num >= integer:
                res += num
                decreasing_num -= integer

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
        if number < self.first_number or number > 9999:
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

        return "".join(res)

    #///////////////////////////////////////////////////////////////////////////
    def getReprLowercaseGreekLetter(self, number):
        """
                HLevel.getReprLowercaseGreekLetter

                number  : (int)
        """
        return self.stringBase( number = number,
                                base = 24,
                                digits = "αβγδεζηθικλμνξοπρστυφχψω" )

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

        for digit in str(strnumber):
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

        for digit in str(strnumber):
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

            if strnumber_index >= len(self.numbers_format):
                msg = "(HLevel.initFromStr) Too many integers in '{0}'; format string='{1}'"
                raise Exception(msg.format(_src,
                                           self.numbers_format))
                                           
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
                self.append( self.getNumberFromLowercRomanNumber( strnumber ))

            elif number_format == '①':
                self.append( self.getNumberFromEnclosedNumber( strnumber ))

            elif number_format == '一':
                self.append( self.getNumberFromJapaneseNumber( strnumber ))

            elif number_format == '¹':
                self.append( self.getNumberFromSuperscriptNumeral( strnumber ))

            elif number_format == '₁':
                self.append( self.getNumberFromSubscriptNumeral( strnumber ))

            elif number_format == '１':
                self.append( self.getNumberFromFullWidthNumeral( strnumber ))

            elif number_format == 'α':
                self.append( self.getNumberFromLowercGreekLetter( strnumber ))

            elif number_format == 'Α':
                self.append( self.getNumberFromCapitalGreekLetter( strnumber ))

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

            elif char not in HLevel.invalid_chars_in_pre_suffix:
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
        (div, mod) = divmod(number - self.first_number, base)
        if div:
            return self.stringBase(div, base, digits) + digits[mod]
        else:
            return digits[mod]

    #///////////////////////////////////////////////////////////////////////////
    def findHLevelStringFromAString(self, src):
        """
                HLevel.findHLevelStringFromAString

                src     : (str)

                Return ( (bool)success,
                         if success, position of the hlevel in <src>,
                         if success, hlevel string,
                       )
        """
        pattern = re.escape(self.prefix)

        for index_numberf, numberf in enumerate(self.numbers_format[::-1]):
            
            if numberf == '1':
                pattern += "[" + "|".join(map(re.escape,HLevel.arabicnumber_symbols)) + "]+"

            elif numberf == 'I':
                pattern += "[" + "|".join(map(re.escape,HLevel.capitalromannumber_symbols)) + "]+"

            if index_numberf+1 < len(self.numbers_format):
                pattern += re.escape(self.separator)

        pattern += re.escape(self.suffix)

        search = re.search(pattern, src)
        if search is None:
            return (False, None, None)
        else:
            return (True,
                    search.start(),
                    src[search.start():search.end()])
