"""
This module contains some open, free-to-use questionnaires in English.
If you want to add your own questionnaire, go ahead and add it to a new file.
For other languages, use appropriate folders.

Every questionnaire should be a function taking name, questionOptions and pageOptions as arguments.
The default name should be uppercase abbreviation of the questionnaire name. The function itself should be
lowercase abbreviation of the questionnaire name. Every function should have a docstring
with APA-style citation of the questionnaire and info what it measures. See RSES as an example.
The default return value should be a PageModel.

I'd be greatful if you could also write a documentation for the questionnaire.
See the repo: https://github.com/jakub-jedrusiak/VelesDocs
"""

from .rses import rses
from .nfcs import nfcs, nfcsShort
from .tls15 import tls15
from .sd3 import sd3
from .tipi import tipi