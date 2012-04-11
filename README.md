zippy
=====

A simple Python for the Ziptastic ZIP Code API search.

```python
>>> import zippy

>>> zippy.do(94155)
{'city': 'SAN FRANCISCO', 'country': 'US', 'state': 'CA'}

>>> zippy.do('94155')
{'city': 'SAN FRANCISCO', 'country': 'US', 'state': 'CA'}

>>> zippy.da(94155)
{'city': 'SAN FRANCISCO', 'country': 'US', 'state': 'CA'}
```
