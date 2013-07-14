from distutils.core import setup

setup(
    name='pywhich',
    version='1.1.1',
    description='Find where python modules are installed.',
    long_description='''\
Thanks to Mark Paschal for taking my 10 line script and adding various useful flags, and dealing with some edge cases.

Code is maintained at: https://github.com/tatwright/pywhich''',
    py_modules=['pywhich'],
    scripts=['bin/pywhich'],
    author='Mark Paschal',
    author_email='markpasc@markpasc.org',
    url='https://github.com/markpasc/pywhich',
    maintainer='Tom Wright',
    maintainer_email='tat.wright@googlemail.com',
    classifiers=[
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ]
)
