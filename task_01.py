#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module converts farenheit into celcius."""


import decimal


ABSOLUTE_DIFFERENCE = decimal.Decimal('273.15')


def fahrenheit_to_celsius(degrees):
    """calculate fahrenheit as celsius. decimal format.

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


def celsius_to_kelvin(degrees):
    """calculate celcius as kelvin. decimal format.

    Args:
      degrees (int): temp value
      ABSOLUTE_DIFFERENCE (dec): value of 273.15

    Returns:
      kelvin (int): 'degrees' + ABSOLUTE_DIFFERENCE

    Examples:
      >>>fahrenheit_to_celsius(212)
      Decimal('100')
    """
    kelvin = (degrees + ABSOLUTE_DIFFERENCE)

    return kelvin
