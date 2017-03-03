#!/usr/bin/env python

from distutils.core import setup

setup(name='py_b',
      version='0.1',
      description='py_b',
      author='Joe Drago',
      author_email='joedrago@gmail.com',
      url='https://www.example.org/',
      packages=['py_b'],
      entry_points={
        'console_scripts': ['py_b=py_b:main'],
      },
      install_requires=['requests==2.1.0'],
     )
