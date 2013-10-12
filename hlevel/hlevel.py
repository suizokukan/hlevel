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

    * HLevelError class
    * HLevel class
"""

################################################################################
class HLevelError(BaseException):
    """
        HLevelError class
    """

    #///////////////////////////////////////////////////////////////////////////
    def __init__(self, message):
        BaseException.__init__(self, message)

################################################################################
class HLevel(list):
    """
        HLevel class
    """

    # default representation of the object :
    defaultformat = ".(1111111111)"

    # accepted numbers in a format string :
    reprnum = [ "1", "I", "i", "A", "a", "①", "一" ]

    #///////////////////////////////////////////////////////////////////////////
    def __init__(self, src=None):
        """
                HLevel.__init__

                src     : (str)
        """
        list.__init__(self)
        
        self.setFormat( HLevel.defaultformat )

        if src is not None:
            self.setData(src)

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

            number_format = self.numbers_format[number_index]

            if number_index+1 > len_numbers_format:
                msg = "HLevel.getRepr : too many digits in {0}; numbers expected are {1}."
                raise HLevelError( msg.format("".join(res),
                                              self.numbers_format))

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
                
            else:
                msg = "HLevel.getRepr : unknown number format '0'; expected formats are {1}."
                raise HLevelError(msg.format(number_format,
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
    def getReprCapitalLetter(self, number):
        """
                HLevel.getReprCapitalLetter

                number  : (int)
        """
        if number < 1 or number > 26:
            msg = "HLevel.getReprCapitalLetter : can interpret number {0} as a capital letter."
            raise HLevelError( msg.format(number) )

        return chr(64 + number)

    #///////////////////////////////////////////////////////////////////////////
    def getReprCapitalRomanNumber(self, number):
        """
                HLevel.getReprCapitalRomanNumber

                number  : (int)
        """
        if number < 1 or number > 1999:
            msg = "HLevel.getReprCapitalRomanNumber : can interpret number {0} as a Roman numeral."
            raise HLevelError( msg.format(number) )
        
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
            msg = "HLevel.getReprEnclosedNumber : can interpret number {0} as an enclosed numeral."
            raise HLevelError( msg.format(number) )

        return chr(0x2460 + number - 1 )

    #///////////////////////////////////////////////////////////////////////////
    def getReprJapaneseNumber(self, number):
        """
                HLevel.getReprJapaneseNumber

                number  : (int)
        """
        if number < 1 or number > 9999:
            msg = "HLevel.getReprJapaneseNumber : can interpret number {0} as a Japanese number."
            raise HLevelError( msg.format(number) )

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
    def getReprLowerCaseLetter(self, number):
        """
                HLevel.getReprLowerCaseLetter

                number  : (int)
        """
        if number < 1 or number > 26:
            msg = "HLevel.getReprLowerCaseLetter : can interpret number {0} as a letter."
            raise HLevelError( msg.format(number) )

        return self.getReprCapitalLetter(number).lower()

    #///////////////////////////////////////////////////////////////////////////
    def getReprLowerCaseRomanNumber(self, number):
        """
                HLevel.getReprLowerCaseRomanNumber

                number  : (int)
        """
        return self.getReprCapitalRomanNumber(number).lower()

    #///////////////////////////////////////////////////////////////////////////
    def setFormat(self, formatstr):
        """
                HLevel.setFormat

                src     : (str)
        """
        if len(formatstr) == 0:
            raise HLevelError( "HLevel.setFormat : empty format string" )

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

            else:
                self.suffix += char
                
