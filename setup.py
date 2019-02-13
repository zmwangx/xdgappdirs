#!/usr/bin/env python
import os
import sys
# appdirs is a dependency of setuptools, so allow installing without it.
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
import ast


def read(fname):
    inf = open(os.path.join(os.path.dirname(__file__), fname))
    out = "\n" + inf.read().replace("\r\n", "\n")
    inf.close()
    return out


# Do not import `xdgappdirs` yet, lest we import some random version on sys.path.
for line in read("xdgappdirs.py").splitlines():
    if line.startswith("__version__"):
        version = ast.literal_eval(line.split("=", 1)[1].strip())
        break

extras_require = {"pathlib": "pathlib2"} if sys.version_info.major == 2 else {}


setup(
    name='xdgappdirs',
    version=version,
    extras_require=extras_require,
    description='A small Python module for determining appropriate ' + \
        'platform-specific dirs, e.g. a "user data dir".',
    long_description=read('README.rst') + '\n' + read('CHANGES.rst'),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords='application directory log cache user',
    author='Zhiming Wang',
    author_email='i@zhimingwang.org',
    url='https://github.com/zmwangx/xdgappdirs',
    license='MIT',
    py_modules=["xdgappdirs"],
)
