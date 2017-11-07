from distutils.core import setup

setup(
    name='mnctools',
    version='0.1',
    packages=['mnctools',],
)


package:
  name: mnctools
  version: "0.1"

source:
  git_url: https://github.com/coecms/mnctools.git

requirements:
  build:
    - python
    - setuptools
  run:
    - python

test:
  imports:
    - mnctools

about:
  home: https://github.com/marshallward/mnctools.git
