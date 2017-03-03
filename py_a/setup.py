#!/usr/bin/env python

from distutils.core import setup

setup(name='py_a',
      version='0.1',
      description='py_a',
      author='Joe Drago',
      author_email='joedrago@gmail.com',
      url='https://www.example.org/',
      packages=['py_a'],
      entry_points={
        'console_scripts': ['py_a=py_a:main'],
      },
      install_requires=['requests==2.13.0'],
     )
