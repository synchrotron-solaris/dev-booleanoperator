#!/usr/bin/env python

"""
This module is responsible for running Device Servers for each class.
"""
from __future__ import absolute_import
import sys

from tango.server import run

from booleanoperator.booleanoperator import BooleanOperator


def run_boolean_operator(args=None, **kwargs):
    """
    Run device server for BooleanOperator device class.

    :param list args: list of command line arguments [default: None, \
    meaning  use sys.argv]
    :param kwargs: for more info look for tango.server.run doc in PyTango
    :return: None
    """
    run((BooleanOperator,), args=args, **kwargs)


def run_all_classes(args=None, **kwargs):
    """
    Run device server for BooleanOperator and other device classes.

    :param list args: list of command line arguments [default: None, \
    meaning  use sys.argv]
    :param kwargs: for more info look for tango.server.run doc in PyTango
    :return: None
    """
    run((BooleanOperator,), args=args, **kwargs)
    # run((BooleanOperator, and, other, classes), args=args, **kwargs)


if __name__ == '__main__':
    run_all_classes(["BooleanOperator"] + sys.argv[1:])
