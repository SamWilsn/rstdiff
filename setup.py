#!/usr/bin/env python

import os

from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


description = (
    "Creates a diff highlighting changes between two reStructuredText inputs"
)

classifiers = [
    "Programming Language :: Python :: 3",
    (
        "License :: "
        "OSI Approved :: "
        "GNU General Public License v2 or later (GPLv2+)"
    ),
]

setup(
    name="rstdiff",
    version="0.5.1",
    description=description,
    long_description=read("README.rst"),
    classifiers=classifiers,
    author="Stefan Merten",
    author_email="smerten@oekonux.de",
    url="https://github.com/SamWilsn/rstdiff",
    license="GPL 2+",
    install_requires=["docutils", "Pygments"],
    packages=["rstdiff", "rstdiff.treediff"],
    entry_points={
        "console_scripts": [
            "rstdiff=rstdiff:main",
        ]
    },
)
