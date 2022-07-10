from importlib.metadata import entry_points
from setuptools import setup

setup(
    name="data_uploads",
    version="0.0.1",
    description="data uploads Management",
    entry_points='''
    [console_scripts]
    data_uploads=data_uploads:web
    ''',
    py_modules=['src'],
    scripts=['data_uploads.py']
)