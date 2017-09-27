from setuptools import setup, find_packages
from os import path

import smartsched

VERSION = smartsched.__version__

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.MD'), encoding='utf-8') as f:
    long_description = f.read()

requirements = [
    "influxdb",
    "xmltodict"
]

setup(name='smartsched',
      version=VERSION,
      description='Basic library for allowing authomatic VMs deployment and migration for the purpose of optimisation.',
      author='JINR LIT Cloud Team',
      author_email='gavelock+jinr@gmail.com',
      url='https://github.com/JINR-LIT/SmartScheduler-Core',
      python_requires='~=3.4',

      classifiers=[
          'Development Status :: 3 - Alpha',

          'Intended Audience :: Developers',
          'Topic :: Software Development',

          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
      ],

      keywords='cloud api scheduler',

      data_files=[('/etc/smartscheduler', ['./config_example.cfg'])],
      include_package_data=True,
      install_requires=requirements,
      extras_require={
          'dev': [
              'pytest',
              'pytest-pep8',
              'pytest-cov',
              'bumpversion',
              'wheel',
              'twine'
          ]
      },
      packages=find_packages(exclude=['tests']))
