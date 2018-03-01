#from setuptools import setup
from distutils.core import setup

setup(
    name='toolbox',
    version='1.1',
    description='toolbox of python scripts',
    url='https://github.com/NapoleonWils0n/toolbox',
    author='NapoleonWils0n',
    maintainer='NapoleonWils0n',
    license='GPL',
    keywords='python toolbox',
    packages=['toolbox'],
    entry_points={
        'console_scripts': [
            'm3u8creator = toolbox.m3u8creator:entry',
        ],
    }
)
