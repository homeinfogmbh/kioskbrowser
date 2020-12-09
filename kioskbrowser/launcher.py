"""Launches the kiosk browser."""

from subprocess import check_call
from sys import exit  # pylint: disable=W0622

from kioskbrowser.config import process


__all__ = ['launch']


def launch():
    """Launches the kiosk browser."""

    returncode = check_call(process())
    exit(returncode)
