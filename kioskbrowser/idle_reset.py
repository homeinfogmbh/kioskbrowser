"""Configures the Idle Reset plugin for chrome / chromium."""

from pathlib import Path

from kioskbrowser.leveldb import LOCALSTORAGE, set_ext_key


__all__ = ['configure']


EXTENSION_ID = 'nnaoeblcffjlledmikadmhhfhjpolcjd'


def configure(**kwargs):
    """Configures the Idle Reset plugin."""

    database = Path.home().joinpath(LOCALSTORAGE)

    for key, value in kwargs.items():
        set_ext_key(database, EXTENSION_ID, key, value)
