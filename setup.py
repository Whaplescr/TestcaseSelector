from distutils.core import setup
from pkgutil import walk_packages
import hotdog

def find_packages(path='.', prefix=""):
    yield prefix
    prefix = prefix + "."
    for _, name, ispkg in walk_packages(path, prefix):
        if ispkg:
            yield name

setup(
  name = 'TestcaseSelector',
  packages = list(find_packages(hotdog.__path__, hotdog.__name__)),
  version = '1.0.0',
  description = 'Unittest test selector window',
  author = 'Charles Whaples',
  author_email = 'whaplescr@gmail.com',
  url = 'https://github.com/Whaplescr/TestcaseSelector',
  download_url = 'https://github.com/Whaplescr/TestcaseSelector/tarball/1.0.0',
  keywords = ['appium', 'selenium', 'testing','unittest'],
  classifiers=[],
  install_requires=[]
)