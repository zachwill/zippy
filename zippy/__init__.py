"""
A simple wrapper for the Ziptastic ZIPCode API.

>>> import zippy
>>> zippy.do('94155')
{'city': 'SAN FRANCISCO', 'country': 'US', 'state': 'CA'}
"""

from . import core
from .core import do, da
