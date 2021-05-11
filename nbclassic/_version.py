# Next beta/alpha/rc release: The version number for beta is X.Y.ZbN **without dots**.

version_info = (0, 2, 7)
__version__ = '.'.join(map(str, version_info[:3])) + ''.join(version_info[3:])
