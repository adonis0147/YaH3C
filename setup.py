#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup
from platform import python_version

if python_version().startswith('2'):
    import yah3c.yah3c

    setup(name='yah3c',
          version=yah3c.yah3c.__version__,
          description='A program for h3c authentication in SYSU east campus.',
          author='maple',
          author_email='maplevalley8@gmail.com',
          url='https://github.com/humiaozuzu/YaH3C',
          download_url='https://github.com/humiaozuzu/YaH3C',
          license='MIT',
          packages=['yah3c', 'yah3c/colorama'],
          scripts=['scripts/yah3c'],
          )
else:
    import yah3c_py3.yah3c

    setup(name='yah3c',
          version=yah3c_py3.yah3c.__version__,
          description='A program for h3c authentication in SYSU east campus.',
          author='maple',
          author_email='maplevalley8@gmail.com',
          url='https://github.com/humiaozuzu/YaH3C',
          download_url='https://github.com/humiaozuzu/YaH3C',
          license='MIT',
          packages=['yah3c_py3', 'yah3c_py3/colorama'],
          scripts=['scripts_py3/yah3c'],
          )
