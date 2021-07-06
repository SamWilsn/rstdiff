#!/usr/bin/env python

import os
from setuptools import setup

from version import version


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='rstdiff',
    version=version,
    description='Tool for creating a diff highlighting changes from two reStructuredText input files',
    long_description=read('README.rst'),
    author='Stefan Merten',
    author_email='smerten@oekonux.de',
    url='https://github.com/SamWilsn/rstdiff',
    license='GPL 2+',
    install_requires=[ 'docutils', 'Pygments' ],
    packages=[ 'rstdiff', 'rstdiff.treediff' ],
    entry_points={
        'console_scripts': [
            'rstdiff=rstdiff:main',
        ]
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)',
    ],
)
