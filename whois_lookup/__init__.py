"""
whois-lookup - Perform WHOIS lookups

Part of Viprasol Utilities: https://viprasol.com
"""

__version__ = "0.1.0"
__author__ = "Viprasol"
__email__ = "hello@viprasol.com"

from .core import WhoisLookup, lookup, process, main

__all__ = ["WhoisLookup", "lookup", "process", "main"]
