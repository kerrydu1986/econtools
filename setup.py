from setuptools import setup, find_packages, Extension
from Cython.Distutils import build_ext

import numpy as np

ext_modules = [Extension('econtools.cframetools', ['econtools/cframetools.pyx'],
                         include_dirs=[np.get_include()])]


def readme():
    with open('README.md') as f:
        return f.read()


setup(name='econtools',
      version='0.0.1',
      description='Econometrics and other tools',
      long_description=readme(),
      # url=
      author='Daniel Sullivan',
      # author_email=
      packages=find_packages(),
      install_requires=[
          'numpy>=1.9.2',
          'pandas>=0.16.0',
          'scipy>=0.15.1',
          'cython>=0.20',
      ],
      test_suite='nose.collector',
      tests_require=['nose'],
      include_package_data=True,        # To copy stuff in `MANIFEST.in`
      cmdclass={'build_ext': build_ext},
      ext_modules=ext_modules,
      # dependency_links=['http://
      # zip_safe=False
      license='BSD'
      )
