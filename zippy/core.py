"""
Core functionality for the Ziptastic ZIPCode API wrapper.
"""

import requests
from simplejson import loads


def do(zipcode):
    """Search for a ZIPCode."""
    if isinstance(zipcode, int):
        zipcode = str(zipcode)
    url = "http://zip.elevenbasetwo.com/?zip=%s" % zipcode
    req = requests.get(url)
    return loads(req.content)


def da(zipcode):
    """Just because."""
    return do(zipcode)
