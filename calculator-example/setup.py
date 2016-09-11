"""
This file has been written with love by Burak Topal (lexygon) for giving a simple example for writing C extensions for Python 3.5.
Feel free to cloning, sharing, editing and committing some new examples.
I have tried to explain each part basicly as I can.
For communicating with me:
mail: hi@buraktopal.xyz
github: github.com/lexygon

For documentation for Python/C API please visit https://docs.python.org/3/c-api/
"""

from distutils.core import setup, Extension

# defining calculator_module as an extension class instance.
# 'calculator' is extension's name and sources is a file name list.
calculator_module = Extension('calculator', sources=['calculator.c'])

# calling setup function with theese parameters.
setup(name='python_c_calculator_extension',
      version='0.1',
      description='An Example For Python C Extensions',
      ext_modules=[calculator_module],
      url='github.com/lexygon',
      author='Burak Topal',
      author_email='hi@buraktopal.xyz')
