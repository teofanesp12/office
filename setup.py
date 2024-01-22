"""
setuptools for office
"""

from setuptools import setup, find_packages
from os import path


def get_long_desc():
    here = path.abspath(path.dirname(__file__))
    with open(path.join(here, 'README.md'), encoding='utf-8') as f:
        return f.read()


setup(name='office',
      version='0.0.1',
      description='For Office',
      url='https://github.com/teofanesp12/office',
      download_url='https://github.com/teofanesp12/office/archive/v0.0.1.tar.gz',
      author='Teofanes Paz',
      author_email='teofanesp12@gmail.com',
      license='AGPL-3.0',
      long_description=get_long_desc(),
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'Topic :: Office/Business',
          'Topic :: Software Development :: Libraries',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.11',
      ],
      keywords='openoffice libreoffice microsoft office outlook',
      packages=find_packages(exclude=['contrib', 'docs', 'tests']),  # Required
      project_urls={
      },
      zip_safe=False)
