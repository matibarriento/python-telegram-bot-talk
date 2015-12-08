#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Class for forms """


class Param(object):

    """Param base class"""

    def __init__(self, index):
        super(Param, self).__init__()
        if index.isdigit():
            self.index = index
        else:
            raise Exception("Index must be a number")
