__author__ = 'Ge Yang'

from setuptools import setup

setup(
    name="dave",
    version="0.1.0",  # dave is always in development mode.
    py_modules=['dave'],
    install_requires=[
        'Click'
    ],
    entry_points='''
        [console_scripts]
        dave=dave:main
    '''
)
