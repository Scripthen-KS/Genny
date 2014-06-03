#!/usr/bin/python
#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# Genny Lib, will only contain string variables and
# calculations and directory options.

# List of to do.
menu_index="""
	Welcome to Genny!
To get started, please read this short story of Genny's life
then you may proceed.

================ Genny ================
Genny is a wee Python script which will generate keys that are from
pre-defined character sets."""

# List of chars-list
menu_opt0="""
Please select your char list, there's 5 to choose from...

  0  Alphabetical keys: a-z (lowercase)
  1  Standard Hexadecimal keys: A-F, 0-9
  2  Number-only keys: 0-9
  3  Alphanumeric keys: A-Z, a-z, 0-9
  4  Alphanumeric + Symbols Keys: a-z, A-Z, 0-9 + All UK keyboard symbols.

"""
# Loop times.
menu_opt1="""
Checkpoint Amount:
Recommended is 100,000 (type: 100000), after this point, generation starts
to slow down.

If you have more than 6GB of FREE system memeory
feel free to set it over 40000000.
"""

menu_opt2="""
Enter key length size, default is 64-bit (8 chars, aaaabbbb)
WPA is 8 - 63 in length

"""

