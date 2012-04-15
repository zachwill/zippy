zippy
=====

A simple Python for the Ziptastic ZIP Code API.

```python
>>> import zippy

>>> zippy.do(94122)
{'city': 'SAN FRANCISCO', 'country': 'US', 'state': 'CA'}

>>> zippy.do('94122')
{'city': 'SAN FRANCISCO', 'country': 'US', 'state': 'CA'}

>>> zippy.da(94122)
{'city': 'SAN FRANCISCO', 'country': 'US', 'state': 'CA'}

>>> zippy.da('94122')
{'city': 'SAN FRANCISCO', 'country': 'US', 'state': 'CA'}
```
