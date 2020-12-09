"""Chromium local storage manipulation."""

from pathlib import Path

from plyvel import DB


__all__ = ['LOCALSTORAGE', 'set_ext_key']


LOCALSTORAGE = Path('.config/chromium/Default/Local Storage/leveldb/')
EXTENSION_SCHEME = '_chrome-extension://'
EXTENSION_SEP = b'\x00\x01'
VALUE_PREFIX = b'\x01'


def get_key(extension: str, key: str) -> bytes:
    """Returns the level DB key for the given key name."""

    prefix = f'{EXTENSION_SCHEME}{extension}'
    return prefix.encode() + EXTENSION_SEP + key.encode()


def get_value(value: object) -> bytes:
    """Returns a leveldb value."""

    return VALUE_PREFIX + str(value).encode()


def set_ext_key(database: Path, extension: str, key: str, value: object):
    """Sets the value to the key of the given extension."""

    DB(str(database)).put(get_key(extension, key), get_value(value))
