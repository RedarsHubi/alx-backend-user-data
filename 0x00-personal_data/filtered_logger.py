#!/usr/bin/env python3
"""
Module for obfuscation
"""
import re


def filter_datum(fields, redaction, message, separator):
    """Obfuscation function"""
    return re.sub(r'(' + '|'.join(map(re.escape, fields)) +
                  r')=[^{}]+'.format(re.escape(separator)),
                  r'\1=' + redaction,
                  message)
