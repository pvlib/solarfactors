# -*- coding: utf-8 -*-

from pvfactors.version import __version__  # noqa: F401
import logging
logging.basicConfig()

try:
    from shapely import geos_version, geos_capi_version  # noqa: F401
except ImportError as err:
    msg = (
        "pvfactors detected that the shapely package is not correctly installed. "
        "Make sure that you installed the prerequisites, including Shapely and "
        "PyGeos, in a supported environment."
    )
    raise ImportError(msg) from err


class PVFactorsError(Exception):
    pass
