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
      kelvin (dec): 'degrees' + ABSOLUTE_DIFFERENCE

    Examples:
      >>>celsius_to_kelvin(100)
      Decimal('373.15')
    """
    kelvin = (degrees + ABSOLUTE_DIFFERENCE)

    return kelvin


def fahrenheit_to_kelvin(degrees):
    """calculate fahrenheit as kelvin. decimal format.

    Args:
      degrees (int): temp value
      ABSOLUTE_DIFFERENCE (dec): value of 273.15
      fahrenheit_to_celsius (func): converts to celsius
      celsius_to_fahrenheit (func): converts to kelvin

    Returns:
      kelvinf (dec): converted to celsius, then to kelvin

    Examples:
      >>>fahrenheit_to_kelvin(212)
      Decimal('373.15')
    """
    kelvinf = celsius_to_kelvin(fahrenheit_to_celsius(degrees))

    return kelvinf
