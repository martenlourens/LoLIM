from setuptools import setup

setup(
    name='LoLIM',
    version="2020.02.03",    
    description='This is a set of scripts used to analyze the data for the LOFAR-LIM (LOFAR for Lightning IMaging) project.',
    url='https://github.com/Bhare8972/LOFAR-LIM',
    author="Brian M. Hare",
    license="MIT License",
    packages=['LoLIM'],
    install_requires=[
        'numpy',
        'matplotlib',
        'scipy',
        'h5py',
        'Cython',
        'PyQt5',
    ], # idk what the correct list of dependencies is... (threse are probably not all of them!)
)
