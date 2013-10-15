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
    ❏HLevel❏ : hlevel/tests.py
"""

import unittest

from hlevel import HLevel

################################################################################
class TESTHLevel(unittest.TestCase):
    """
        class TESTHLevel
    """

    #///////////////////////////////////////////////////////////////////////////
    def test_prefix_suffix_separator(self):
        """
                TESTHLevel.test_prefix_suffix_separator
        """
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        hlevel = HLevel( src="(α.αα.ααα)",
                     formatstr = ".(α.α.α)",
                     first_number = 1)

        self.assertEqual( hlevel.prefix, '(' )
        self.assertEqual( hlevel.suffix, ')' )
        self.assertEqual( hlevel.separator, '.' )

        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        hlevel = HLevel( src="α.αα.ααα",
                     formatstr = ".α.α.α",
                     first_number = 1)

        self.assertEqual( hlevel.prefix, '' )
        self.assertEqual( hlevel.suffix, '' )
        self.assertEqual( hlevel.separator, '.' )

        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        hlevel = HLevel( src="{{α.αα.ααα",
                     formatstr = ".{{α.α.α",
                     first_number = 1)

        self.assertEqual( hlevel.prefix, '{{' )
        self.assertEqual( hlevel.suffix, '' )
        self.assertEqual( hlevel.separator, '.' )

        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        hlevel = HLevel( src="α.αα.ααα}}",
                     formatstr = ".α.α.α}}",
                     first_number = 1)

        self.assertEqual( hlevel.prefix, '' )
        self.assertEqual( hlevel.suffix, '}}' )
        self.assertEqual( hlevel.separator, '.' )

        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        hlevel = HLevel( src="()",
                     formatstr = ".(α.α.α)",
                     first_number = 1)

        self.assertEqual( hlevel.prefix, '(' )
        self.assertEqual( hlevel.suffix, ')' )
        self.assertEqual( hlevel.separator, '.' )

    #///////////////////////////////////////////////////////////////////////////
    def test_comparison(self):
        """
                TESTHLevel.test_comparison
        """
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        hlevel1 = HLevel( src="(1.11.999.2.9999)",
                      formatstr = ".(1.1.1.1.1)",
                      first_number = 1)

        hlevel2 = HLevel( src="(1.11.999.2.9999)",
                      formatstr = ".(1.1.1.1.1)",
                      first_number = 1)

        self.assertTrue( hlevel1 == hlevel2 )

        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        hlevel1 = HLevel( src="(1.11.999.2.9999)",
                      formatstr = ".(1.1.1.1.1)",
                      first_number = 1)

        hlevel2 = HLevel( src="(1.12.999.2.9999)",
                      formatstr = ".(1.1.1.1.1)",
                      first_number = 1)

        self.assertTrue( hlevel1 < hlevel2 )

        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        hlevel1 = HLevel( src="(1.11.999.2.9999)",
                      formatstr = ".(1.1.1.1.1)",
                      first_number = 1)

        hlevel2 = HLevel( src="(1.11.999.0.9999)",
                      formatstr = ".(1.1.1.1.1)",
                      first_number = 1)

        self.assertTrue( hlevel1 > hlevel2 )

    #///////////////////////////////////////////////////////////////////////////
    def test_ArabicNumbers(self):
        """
                TESTHLevel.test_ArabicNumbers
        """
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        hlevel1 = HLevel( src="(1.11.999.2.9999)",
                      formatstr = ".(1.1.1.1.1)",
                      first_number = 1)

        hlevel2 = HLevel( src = str(hlevel1),
                      formatstr = ".(1.1.1.1.1)",
                      first_number = 1)

        self.assertEqual( str(hlevel1), str(hlevel2) )

        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        hlevel1 = HLevel( src="(5.33.2.1.5)",
                      formatstr = ".(1.1.1.1.1)",
                      first_number = 1)

        hlevel2 = HLevel( src = str(hlevel1),
                      formatstr = ".(1.1.1.1.1)",
                      first_number = 1)

        self.assertEqual( str(hlevel1), str(hlevel2) )

    #///////////////////////////////////////////////////////////////////////////
    def test_CapitalLetters(self):
        """
                TESTHLevel.test_CapitalLetters
        """
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        hlevel1 = HLevel( src="(A.ZZ.ABG.D.GMOQ)",
                      formatstr = ".(A.A.A.A.A)",
                      first_number = 1)

        hlevel2 = HLevel( src="(A.ZZ.ABG.D.GMOQ)",
                      formatstr = ".(A.A.A.A.A)",
                      first_number = 1)

        self.assertEqual( str(hlevel1), str(hlevel2) )

        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        hlevel1 = HLevel( src="(A.ZZ.ABG.D.GMOQ)",
                      formatstr = ".(A.A.A.A.A)",
                      first_number = 1)

        hlevel2 = HLevel( src = str(hlevel1),
                      formatstr = ".(A.A.A.A.A)",
                      first_number = 1)

        self.assertEqual( str(hlevel1), str(hlevel2) )

    #///////////////////////////////////////////////////////////////////////////
    def test_LowerCaseLetters(self):
        """
                TESTHLevel.test_LowerCaseLetters
        """
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        hlevel1 = HLevel( src="(a.zz.abg.g.sdfs)",
                      formatstr = ".(a.a.a.a.a)",
                      first_number = 1)

        hlevel2 = HLevel( src="(a.zz.abg.g.sdfs)",
                      formatstr = ".(a.a.a.a.a)",
                      first_number = 1)

        self.assertEqual( str(hlevel1), str(hlevel2) )

        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        hlevel1 = HLevel( src="(l.id.odm.z.ksfg)",
                      formatstr = ".(a.a.a.a.a)",
                      first_number = 1)

        hlevel2 = HLevel( src = str(hlevel1),
                      formatstr = ".(a.a.a.a.a)",
                      first_number = 1)

        self.assertEqual( str(hlevel1), str(hlevel2) )

    #///////////////////////////////////////////////////////////////////////////
    def test_RomanNumbers(self):
        """
                TESTHLevel.test_RomanNumbers
        """
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        hlevel1 = HLevel( src="(I.IX.MMDCIII.LIX.MMCMXCIX)",
                      formatstr = ".(I.I.I.I.I)",
                      first_number = 1)

        hlevel2 = HLevel( src="(I.IX.MMDCIII.LIX.MMCMXCIX)",
                      formatstr = ".(I.I.I.I.I)",
                      first_number = 1)

        self.assertEqual( str(hlevel1), str(hlevel2) )

        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        hlevel1 = HLevel( src="(I.IX.MMDCIII.LIX.MMCMXCIX)",
                      formatstr = ".(I.I.I.I.I)",
                      first_number = 1)

        hlevel2 = HLevel( src = str(hlevel1),
                      formatstr = ".(I.I.I.I.I)",
                      first_number = 1)

        self.assertEqual( str(hlevel1), str(hlevel2) )

    #///////////////////////////////////////////////////////////////////////////
    def test_LowerCRomanNumbers(self):
        """
                TESTHLevel.test_LowerCRomanNumbers
        """
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        hlevel1 = HLevel( src="(i.ix.mmdciii.lix.mmcmxcix)",
                      formatstr = ".(i.i.i.i.i)",
                      first_number = 1)

        hlevel2 = HLevel( src="(i.ix.mmdciii.lix.mmcmxcix)",
                      formatstr = ".(i.i.i.i.i)",
                      first_number = 1)

        self.assertEqual( str(hlevel1), str(hlevel2) )

        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        hlevel1 = HLevel( src="(i.ix.mmdciii.lix.mmcmxcix)",
                      formatstr = ".(i.i.i.i.i)",
                      first_number = 1)

        hlevel2 = HLevel( src = str(hlevel1),
                      formatstr = ".(i.i.i.i.i)",
                      first_number = 1)

        self.assertEqual( str(hlevel1), str(hlevel2) )

    #///////////////////////////////////////////////////////////////////////////
    def test_EnclosedLetters(self):
        """
                TESTHLevel.test_EnclosedLetters
        """
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        hlevel1 = HLevel( src="(⑩.⑬.③.①.⑳)",
                      formatstr = ".(①.①.①.①.①)",
                      first_number = 1)

        hlevel2 = HLevel( src="(⑩.⑬.③.①.⑳)",
                      formatstr = ".(①.①.①.①.①)",
                      first_number = 1)

        self.assertEqual( str(hlevel1), str(hlevel2) )

        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        hlevel1 = HLevel( src="(⑩.⑬.③.①.⑳)",
                      formatstr = ".(①.①.①.①.①)",
                      first_number = 1)

        hlevel2 = HLevel( src = str(hlevel1),
                      formatstr = ".(①.①.①.①.①)",
                      first_number = 1)

        self.assertEqual( str(hlevel1), str(hlevel2) )
        
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        with self.assertRaises(Exception):
            HLevel( src="(⑩.⑬.③.①①.⑳)",
                    formatstr = ".(①.①.①.①.①)" )
            
    #///////////////////////////////////////////////////////////////////////////
    def test_JapaneseNumbers(self):
        """
                TESTHLevel.test_JapaneseNumbers
        """
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        hlevel1 = HLevel( src="(一.二千二十五.四百六十九.三百二.百五十一)",
                      formatstr = ".(一.一.一.一.一)",
                      first_number = 1)

        hlevel2 = HLevel( src="(一.二千二十五.四百六十九.三百二.百五十一)",
                      formatstr = ".(一.一.一.一.一)",
                      first_number = 1)

        self.assertEqual( str(hlevel1), str(hlevel2) )

        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        hlevel1 = HLevel( src="(一.二千二十五.四百六十九.三百二.百五十一)",
                      formatstr = ".(一.一.一.一.一)",
                      first_number = 1)

        hlevel2 = HLevel( src = str(hlevel1),
                      formatstr = ".(一.一.一.一.一)",
                      first_number = 1)

        self.assertEqual( str(hlevel1), str(hlevel2) )

        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        hlevel1 = HLevel( src="(一.二千二十五.四百六十九.〇)",
                      formatstr = ".(一.一.一.一.一)",
                      first_number = 0)

        hlevel2 = HLevel( src = str(hlevel1),
                      formatstr = ".(一.一.一.一.一)",
                      first_number = 0)

        self.assertEqual( str(hlevel1), str(hlevel2) )

    #///////////////////////////////////////////////////////////////////////////
    def test_SuperscriptNumbers(self):
        """
                TESTHLevel.test_SuperscriptNumbers
        """
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        hlevel1 = HLevel( src="(¹.⁴²⁴.⁴⁰⁹.⁴⁰⁵.⁴⁹⁰)",
                      formatstr = ".(¹.¹.¹.¹.¹)",
                      first_number = 1)

        hlevel2 = HLevel( src="(¹.⁴²⁴.⁴⁰⁹.⁴⁰⁵.⁴⁹⁰)",
                      formatstr = ".(¹.¹.¹.¹.¹)",
                      first_number = 1)

        self.assertEqual( str(hlevel1), str(hlevel2) )

        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        hlevel1 = HLevel( src="(¹.⁴²⁴.⁴⁰⁹.⁴⁰⁵.⁴⁹⁰)",
                      formatstr = ".(¹.¹.¹.¹.¹)",
                      first_number = 1)

        hlevel2 = HLevel( src = str(hlevel1),
                     formatstr = ".(¹.¹.¹.¹.¹)",
                      first_number = 1)

        self.assertEqual( str(hlevel1), str(hlevel2) )

    #///////////////////////////////////////////////////////////////////////////
    def test_SubscriptNumbers(self):
        """
                TESTHLevel.test_SubscriptNumbers
        """
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        hlevel1 = HLevel( src="(₁₀.₉₄₀.₄₈₀₁.₄.₁)",
                      formatstr = ".(₁.₁.₁.₁.₁)",
                      first_number = 1)

        hlevel2 = HLevel( src="(₁₀.₉₄₀.₄₈₀₁.₄.₁)",
                      formatstr = ".(₁.₁.₁.₁.₁)",
                      first_number = 1)

        self.assertEqual( str(hlevel1), str(hlevel2) )

        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        hlevel1 = HLevel( src="(₁₀.₉₄₀.₄₈₀₁.₄.₁)",
                      formatstr = ".(₁.₁.₁.₁.₁)",
                      first_number = 1)

        hlevel2 = HLevel( src = str(hlevel1),
                      formatstr = ".(₁.₁.₁.₁.₁)",
                      first_number = 1)

        self.assertEqual( str(hlevel1), str(hlevel2) )

    #///////////////////////////////////////////////////////////////////////////
    def test_FullWidthNumbers(self):
        """
                TESTHLevel.test_FullWidthNumbers
        """
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        hlevel1 = HLevel( src="(１.３１３９.９１９.１３.９)",
                      formatstr = ".(１.１.１.１.１)",
                      first_number = 1)

        hlevel2 = HLevel( src="(１.３１３９.９１９.１３.９)",
                      formatstr = ".(１.１.１.１.１)",
                      first_number = 1)

        self.assertEqual( str(hlevel1), str(hlevel2) )

        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        hlevel1 = HLevel( src="(１.３１３９.９１９.１３.９)",
                      formatstr = ".(１.１.１.１.１)",
                      first_number = 1)

        hlevel2 = HLevel( src = str(hlevel1),
                      formatstr = ".(１.１.１.１.１)",
                      first_number = 1)

        self.assertEqual( str(hlevel1), str(hlevel2) )

    #///////////////////////////////////////////////////////////////////////////
    def test_LowercGreekLetters(self):
        """
                TESTHLevel.test_LowercGreekLetters
        """
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        hlevel1 = HLevel( src="(α.γωεα.γα.γ.α)",
                      formatstr = ".(α.α.α.α.α)",
                      first_number = 1)

        hlevel2 = HLevel( src="(α.γωεα.γα.γ.α)",
                      formatstr = ".(α.α.α.α.α)",
                      first_number = 1)

        self.assertEqual( str(hlevel1), str(hlevel2) )

        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        hlevel1 = HLevel( src="(α.γωεα.γα.γ.α)",
                      formatstr = ".(α.α.α.α.α)",
                      first_number = 1)

        hlevel2 = HLevel( src = str(hlevel1),
                      formatstr = ".(α.α.α.α.α)",
                      first_number = 1)

        self.assertEqual( str(hlevel1), str(hlevel2) )

    #///////////////////////////////////////////////////////////////////////////
    def test_CapitalGreekLetters(self):
        """
                TESTHLevel.test_CapitalGreekLetters
        """
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        hlevel1 = HLevel( src="(Α.ΓΩΕΑ.ΓΑ.Γ.Α)",
                      formatstr = ".(Α.Α.Α.Α.Α)",
                      first_number = 1)

        hlevel2 = HLevel( src="(Α.ΓΩΕΑ.ΓΑ.Γ.Α)",
                      formatstr = ".(Α.Α.Α.Α.Α)",
                      first_number = 1)

        self.assertEqual( str(hlevel1), str(hlevel2) )

        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        hlevel1 = HLevel( src="(Α.ΓΩΕΑ.ΓΑ.Γ.Α)",
                      formatstr = ".(Α.Α.Α.Α.Α)",
                      first_number = 1)

        hlevel2 = HLevel( src = str(hlevel1),
                      formatstr = ".(Α.Α.Α.Α.Α)",
                      first_number = 1)

        self.assertEqual( str(hlevel1), str(hlevel2) )
