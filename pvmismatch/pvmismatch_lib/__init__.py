# -*- coding: utf-8 -*-
"""
This is the PVMismatch Library. Configuration constants and classes like
:class:`~pvmismatch.pvmismatch_lib.pvconstants.PVconstants`,
:class:`~pvmismatch.pvmismatch_lib.pvcell.PVcell`,
:class:`~pvmismatch.pvmismatch_lib.pvmodule.PVmodule`,
:class:`~pvmismatch.pvmismatch_lib.pvstring.PVstring` and
:class:`~pvmismatch.pvmismatch_lib.pvsystem.PVsystem`, objects are all defined
here.
"""

# imports, version and other info moved to package top level

# TODO: move pvconstants here

# import matplotlib in try: except so tests can run in a virtualenv on Mac OS X
pyplot_error = NotImplementedError
try:
    from matplotlib import pyplot as pyplot_module
except RuntimeError as exc:
    pyplot_module = None
    pyplot_error = exc


def requires_matplotlib(func):
    """
    Decorator raises RuntimeError if matplotlib not installed as Framework on
    Mac OS X, for example if running from virtualenv.
    """
    def wrapper(*args, **kwargs):
        if not pyplot_module:
            raise pyplot_error
        return func(*args, *kwargs)
    return wrapper