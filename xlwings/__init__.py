from __future__ import absolute_import
import sys

__version__ = '0.2.4dev'

# Python 2 vs 3
PY3 = sys.version_info[0] == 3

if PY3:
    string_types = str
else:
    string_types = basestring

# Platform specifics
if sys.platform.startswith('win'):
    from . import _xlwindows as xlplatform
else:
    from . import _xlmac as xlplatform

time_types = xlplatform.time_types

# API
from .main import Workbook, Range, Chart, Sheet
from .constants import *