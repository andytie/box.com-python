from distutils.core import setup
from setuptools import find_packages

setup(name='box',
      version='0.1',
      description='box.com python librairy',
      author='Vincent Jauneau',
      author_email='vincent.jauneau@platypus-creation.com',
      url='https://github.com/platypus-creation/box.com-python',
      license='MIT',
      packages=find_packages(),
      install_requires=['git+git://github.com/requests/requests-oauthlib.git',]
)
