#!/usr/bin/env python

from setuptools import setup

from menu import VERSION_STRING

setup(name='django-simple-menu2',
      packages=['menu'],
      include_package_data=True,
      version=VERSION_STRING,
      description='Simple, yet powerful, code-based menus for Django applications',
      long_description=open('README.rst').read(),
      author='Evan Borgstrom',
      author_email='evan@fatbox.ca',
      url='https://github.com/trbs/django-simple-menu',
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Framework :: Django',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: BSD License',
          'Natural Language :: English',
          'Topic :: Software Development :: Libraries',
          'Topic :: Software Development :: Libraries :: Python Modules',
      ],
      install_requires=['setuptools', 'django>=1.3'])
