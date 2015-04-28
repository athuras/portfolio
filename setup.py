from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'DESCRIPTION.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='portfolio',
    version='0.0.1',
    description='Portfolio optimization for the risk averse.',
    long_description=long_description,
    url='https://github.com/athuras/portfolio',
    author='Alexander Huras',
    author_email='athuras@gmail.com',
    license='MIT',
    classifiers=[
        'Finance',
        'Optimization',
        'ETF'
        ],
    packages=['portfolio'],
    install_requires=['numpy', 'docopt', 'pandas', 'matplotlib', 'seaborn'],
    package_dir={'portfolio': 'portfolio'}
)
