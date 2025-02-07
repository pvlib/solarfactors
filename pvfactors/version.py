from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("solarfactors")
except PackageNotFoundError:
    __version__ = "0+unknown"
