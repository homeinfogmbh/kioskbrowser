#! /usr/bin/env python
"""Installation script."""

from setuptools import setup

setup(
    name='kioskbrowser',
    version_format='{tag}',
    setup_requires=['setuptools-git-version'],
    author='HOMEINFO - Digitale Informationssysteme GmbH',
    author_email='info@homeinfo.de',
    maintainer='Richard Neumann',
    maintainer_email='mail@richard-neumann.de',
    python_requires='>=3.8',
    packages=['kioskbrowser'],
    scripts=['files/kioskbrowser'],
    url='https://github.com/homeinfogmbh/kioskbrowser',
    license='GPLv3',
    description='A kiosk browser solution based on chromium.',
    keywords='kiosk browser chromium'
)
