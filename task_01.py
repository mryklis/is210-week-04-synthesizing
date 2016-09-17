#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module converts farenheit into celcius."""


import decimal


def fahrenheit_to_celsius(degrees):
    """calculate temperature and return as celsius.
    decimal format.

    Args:
      degrees (int): temp value

    Returns:
      converted (int): 'degrees' less 32, multiplied by 5,
      and finally divided by 9

    Examples:
      >>>fahrenheit_to_celsius(212)
      Decimal('100')
    """
    converted = (((decimal.Decimal(degrees) - 32) * 5) / 9)
    return converted
