#!/usr/bin/env python
# -*- coding: utf-8 -*-
from distutils.command.install import INSTALL_SCHEMES
from distutils.core import setup
import os
import sys

__author__ = 'g.bronzini'


def fullsplit(path, result=None):
    """
    Split a pathname into components (the opposite of os.path.join) in a
    platform-neutral way.
    """
    if result is None:
        result = []
    head, tail = os.path.split(path)
    if head == '':
        return [tail] + result
    if head == path:
        return result
    return fullsplit(head, [tail] + result)

# Tell distutils to put the data_files in platform-specific installation
# locations. See here for an explanation:
# http://groups.google.com/group/comp.lang.python/browse_thread/thread/35ec7b2fed36eaec/2105ee4d9e8042cb
for scheme in INSTALL_SCHEMES.values():
    scheme['data'] = scheme['purelib']

# Compile the list of packages available, because distutils doesn't have
# an easy way to do this.
packages, data_files = [], []
root_dir = os.path.dirname(__file__)


def scan_dir( target, packages=[], data_files=[] ):
    for dirpath, dirnames, filenames in os.walk(target):
        # Ignore dirnames that start with '.'
        for i, dirname in enumerate(dirnames):
            if dirname.startswith('.'): del dirnames[i]
        if '__init__.py' in filenames:
            packages.append('.'.join(fullsplit(dirpath)))
        elif filenames:
            data_files.append([dirpath, [os.path.join(dirpath, f) for f in filenames]])
    return packages, data_files

packages, data_files = scan_dir('wizdict')

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
    packages=packages,
#    cmdclass=cmdclasses,
    data_files=data_files,
    platforms=['linux'],
    package_data={
    },
    scripts=[
             ],
    # zip_safe=False,
    install_requires = [
     ],
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
