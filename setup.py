__author__ = 'Ge Yang'

from setuptools import setup

setup(
    name="dave",
    version="0.1.0",  # dave is always un development.
    py_modules=['dave_cli', 'dave_server'],
    install_requires=[
        'Click'
    ],
    entry_points='''
        [console_scripts]
        dave=dave_cli.dave:cli
        dave-server=dave_server.server:start_server
    '''
)
