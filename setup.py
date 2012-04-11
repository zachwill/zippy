"""
Setup and installation for the package.
"""

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name="zippy",
    version="0.1",
    url="http://github.com/zachwill/zippy",
    author="Zach Williams",
    author_email="hey@zachwill.com",
    description="A simple wrapper for the Ziptastic ZIPCode Search API.",
    packages=[
        'zippy'
    ],
    install_requires=[
        'mock',
        'requests',
        'simplejson',
    ],
    license='MIT',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
)
