from setuptools import setup
from setuptools.command.build_py import build_py as _build

from os import path
from io import open

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='UTF8') as f:
    long_description = f.read()


setup(
    name='blindSpot',
    version='1.0.0',
    description='A simple script for construction of mosaic images in python.',
    long_description=long_description,
    url='https://github.com/HamidrezaMoradi/blindSpot',
    author='Hamidreza Moradi',
    author_email='realhamidrezamoradi@gmail.com',
    scripts = ['blindspot'],
    python_requires='>=3.7.0',
    packages=['blindSpot'],
    install_requires=['maths',
                'glob3',
                'systemd-python',
                'Pillow>=6.1.0']
)