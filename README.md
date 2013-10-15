hlevel
======

A (Python3, GPLv3) very simple library allowing to read/write and compare "Hierarchical Level" objects like "1.2.3", "A.IV.6.b" and so on.

Known formats :
---------------

```
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

    * fullwidth_symbols = ("０", "１", "２", "３", "４", "５", "６", "７", "８", "９", "１０", ...)
      negative, null or positive integers

    * lowercasegreek_symbols = ( "α", "β", "γ", "δ", "ε", "ζ", ..., "χ", "ψ", "ω", "αα", ... )
      positive integers, normally greater than zero (but see self.first_number)

    * capitalgreek_symbols = ( "Α", "Β", "Γ", "Δ", "Ε", "Ζ", ..., "Φ", "Χ", "Ψ", "Ω", "ΑΑ", ... )
      positive integers, normally greater than zero (but see self.first_number)
```

A basic example :
-----------------

```python
# separator = '.' ; suffix = ']', no prefix :
hl1 = HLevel( src="C.IX.3]",
              formatstr = ".A.I.1]" )

# separator = '.' ; suffix = ')', prefix = '('
hl2 = HLevel( src="(C.IX.3)",
              formatstr = ".(A.I.1)" )

# although the representations differ, we can compare these two objects :
print(hl1 == hl2)       # renvoie True

# representation :
print( hl1 )   # "C.IX.3]"
print( hl2 )   # "(C.IX.3)"
```

A slightly more complex example (HLevel is derived from list) :
---------------------------------------------------------------

```python
hl1 = HLevel( formatstr = ".①.1.a)" )
hl1.append(13)
hl1.append(2)
hl1.append(3)
# hl1 ~ 13.2.3

hl2 = HLevel( src="<<②|99|z>>",
              formatstr = "|<<①|1|a>>" )
# hl2 ~ 2.99.26


print( hl1 > hl2 )  # True
print( hl1 )        # ⑬.2.c)
print( hl2 )        # <<②|99|z>>
```

 

 
