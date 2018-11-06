from setuptools import setup, find_packages
import os

BASE_DIRECTORY = os.path.dirname(os.path.abspath(__file__))


def get_version():
    version_info = {}
    with open(os.path.join(BASE_DIRECTORY, 'dewds', 'version.py')) as f:
        exec(f.read(), version_info)
    return version_info['__version__']


setup(
    name='dewds',
    version=get_version(),
    packages=find_packages(),
    description='Digital circuit Emulator With programmable Device Support',
    url='https://github.com/dewds/dewds',
    license='MIT',
    author='Nachshon David Armon',
    author_email='nachshon.armon@gmail.com',
)
