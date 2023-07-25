"""Launches the kiosk browser."""

from subprocess import check_call

from kioskbrowser.config import get_command


__all__ = ["launch"]


def launch() -> int:
    """Launches the kiosk browser."""

    return check_call(get_command())
