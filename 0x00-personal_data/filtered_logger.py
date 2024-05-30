#!/usr/bin/env python3
"""
Module for obfuscation
"""
import re
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """Obfuscation function"""
    return re.sub(r'(' + '|'.join(map(re.escape, fields)) +
                  r')=[^{}]+'.format(re.escape(separator)),
                  r'\1=' + redaction,
                  message)
