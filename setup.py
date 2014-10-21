#!/usr/bin/env python
# -*- coding: utf-8 -*-
from distutils.core import setup

from wizdict import __VERSION__
NAME = "wizdict"


setup(
    name=NAME,
    version=__VERSION__,
    download_url='#',
    author='G.Bronzini',
    author_email='g.bronzini@gmail.com',
    license="http://creativecommons.org/licenses/by-nc/3.0/",
    description='Wizard Dictionaries, advanced dictionaries utilities for Python',
    platforms=['linux'],
    packages=['wizdict'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Python Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Creative Commons 3.0',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
        'Programming Language :: Python :: 2.7',
        ],
)
