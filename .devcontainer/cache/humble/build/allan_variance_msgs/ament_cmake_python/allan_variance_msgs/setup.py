from setuptools import find_packages
from setuptools import setup

setup(
    name='allan_variance_msgs',
    version='0.0.0',
    packages=find_packages(
        include=('allan_variance_msgs', 'allan_variance_msgs.*')),
)
