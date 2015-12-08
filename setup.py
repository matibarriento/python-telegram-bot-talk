#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

requirements = [
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='python-telegram-bot-talk',
    version='0.0.1',
    description="Helper to make telegram bot remember the flow of the conversation or current command with params",
    long_description=readme + '\n\n' + history,
    author="Matias Barriento",
    author_email='elmatibarriento@gmail.com',
    url='https://github.com/matibarriento/python-telegram-bot-talk',
    packages=[
        'python-telegram-bot-talk',
    ],
    package_dir={'python-telegram-bot-talk':
                 'python-telegram-bot-talk'},
    include_package_data=True,
    install_requires=requirements,
    license="ISCL",
    zip_safe=False,
    keywords='python-telegram-bot-talk',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
