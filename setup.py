#! /usr/bin/env python
"""Installation script."""

from setuptools import setup

setup(
    name="kioskbrowser",
    use_scm_version={"local_scheme": "node-and-timestamp"},
    setup_requires=["setuptools_scm"],
    author="HOMEINFO - Digitale Informationssysteme GmbH",
    author_email="info@homeinfo.de",
    maintainer="Richard Neumann",
    maintainer_email="mail@richard-neumann.de",
    python_requires=">=3.8",
    install_requires=["plyvel"],
    packages=["kioskbrowser"],
    entry_points={"console_scripts": ["kioskbrowser = kioskbrowser:launch"]},
    url="https://github.com/homeinfogmbh/kioskbrowser",
    license="GPLv3",
    description="A kiosk browser solution based on chromium.",
    keywords="kiosk browser chromium",
)
