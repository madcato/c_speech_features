#! /usr/bin/env python

from setuptools import setup, find_packages, Extension

import os
import numpy

try:
    numpy_include = numpy.get_include()
except AttributeError:
    numpy_include = numpy.get_numpy_include()

_c_speech_features = Extension('_c_speech_features',
        ['python/c_speech_features.i', 'python/helper.c'],
        include_dirs = [numpy_include],
        libraries = ['c_speech_features_static']
        )

setup(name = 'c_speech_features',
      description = 'A C re-implementation of python_speech_features',
      author = 'Chris Lord',
      author_email='chrislord.net@gmail.com',
      version = '0.4.1',
      packages = find_packages(),
      license = 'MIT',
      url = 'https://gitlab.com/Cwiiis/c_speech_features',
      ext_modules = [_c_speech_features]
      )
