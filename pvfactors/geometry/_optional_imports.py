"""Utility module for handling optional dependencies for plotting functionality."""

import functools


def _matplotlib_import_error_message():
    """Generate helpful error message for missing matplotlib."""
    return (
        "matplotlib is required for plotting functionality. "
        "Install it using one of the following methods:\n"
        "  pip install solarfactors[plot]\n"
        "  pip install matplotlib\n"
        "  conda install matplotlib"
    )


def _check_matplotlib():
    """
    Check if matplotlib is available and raise ImportError if not.
    """
    try:
        import matplotlib  # noqa: F401

        return True
    except ImportError:
        raise ImportError(_matplotlib_import_error_message())


def requires_matplotlib(func):
    """Decorator to check for matplotlib availability before executing
    plotting functions.

    Parameters
    ----------
    func : callable
        Function that requires matplotlib

    Returns
    -------
    callable
        Wrapped function that checks for matplotlib before execution
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        _check_matplotlib()
        return func(*args, **kwargs)

    return wrapper


def optional_matplotlib_import():
    """Import matplotlib.pyplot with optional handling.

    Returns
    -------
    module or None
        matplotlib.pyplot module if available, None otherwise

    Raises
    ------
    ImportError
        If matplotlib is not available with helpful installation message
    """
    _check_matplotlib()
    import matplotlib.pyplot as plt  # noqa: F401

    return plt
