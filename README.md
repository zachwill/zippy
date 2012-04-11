zippy
=====

A simple Python for the Ziptastic ZIP Code API search.

```python
>>> import zippy

>>> zippy.do(94155)
{'SF': {'ZIPCode': 'data'}}

>>> zippy.do('94155')
{'SF': {'ZIPCode': 'data'}}

>>> zippy.da(94155)
{'SF': {'ZIPCode': 'data'}}
```
