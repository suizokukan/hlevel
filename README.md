hlevel
======

A (Python3, GPLv3) very simple library allowing to read/write and compare "Hierarchical Level" objects like "1.2.3", "A.IV.6.b" and so on.

A basic example :

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
print( hl1.getRepr() )   # "C.IX.3]"
print( hl2.getRepr() )   # "(C.IX.3)"
```

A slightly more complex example (HLevel is derived from list) :

```python
hl1 = HLevel( formatstr = ".①.1.a)" )
hl1.append(13)
hl1.append(2)
hl1.append(3)
# hl1 ~ 13.2.3

hl2 = HLevel( src="<<②|99|z>>",
              formatstr = "|<<①|1|a>>" )
# hl2 ~ 2.99.26


print( hl1 > hl2 )            # True
print( hl1.getRepr() )        # ⑬.2.c)
print( hl2.getRepr() )        # <<②|99|z>>
```

 

 
