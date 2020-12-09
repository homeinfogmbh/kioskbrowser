"""Chromium local storage manipulation."""

from configparser import NoOptionError, ConfigParser
from logging import DEBUG, INFO, basicConfig, getLogger
from pathlib import Path
from sys import exit  # pylint: disable=W0622
from typing import List
from urllib.parse import urlparse

from kioskbrowser.idle_reset import configure


__all__ = ['process']


CHROMIUM = '/usr/bin/chromium'
CONFIG_FILE = Path('/usr/local/etc/kioskbrowser.conf')
LOGGER = getLogger(__file__)


def process() -> List[str]:
    """Start the kiosk browser."""

    config = ConfigParser()

    if not config.read(CONFIG_FILE):
        LOGGER.error('Cannot read config file.')
        exit(1)

    debug = config.getboolean('kiosk', 'debug', fallback=False)
    basicConfig(level=DEBUG if debug else INFO)
    chromium = config.get('kiosk', 'chromium', fallback=CHROMIUM)
    command = [chromium,'--kiosk', '--fullscreen']

    try:
        url = config.get('kiosk', 'url')
    except NoOptionError:
        LOGGER.error('No URL specified.')
        exit(2)

    timeout = config.getint('kiosk', 'timeout', fallback=30)
    configure(url=url, seconds=timeout)

    if config.getboolean('kiosk', 'incognito', fallback=False):
        command.append('--incognito')

    command.append(url)

    if config.getboolean('kiosk', 'extensions', fallback=False):
        command.append('--enable-extensions')

    command.append(url)

    if config.getboolean('kiosk', 'file-access-from-files', fallback=False):
        command.append('--allow-file-access-from-files')

    command.append(url)

    if config.getboolean('kiosk', 'disable-web-security', fallback=False):
        command.append('--disable-web-security')

    command.append(url)
    resolution = config.get('kiosk', 'resolution', fallback='1920,1080')
    command.append(f'--window-size={resolution}')
    position = config.get('kiosk', 'position', fallback='0,0')
    command.append(f'--window-position={position}')
    host = urlparse(url).netloc
    host_rules = [f'MAP * {host}']

    for exclude in config.get('kiosk', 'exclude', fallback='').split():
        host_rules.append(f'EXCLUDE {exclude}')

    host_rules = ', '.join(host_rules)
    command.append(f'--host-resolver-rules={host_rules}')
    LOGGER.debug('Assembled command: %s', command)
    return command
