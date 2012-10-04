#!/usr/bin/env python

from nose.plugins.errorclass import ErrorClass, ErrorClassPlugin

import os, sys, inspect

def execution_path(filename):
    return os.path.join(os.path.dirname(sys._getframe(1).f_code.co_filename), filename)

class Todo(Exception):
    pass

class TodoPlugin(ErrorClassPlugin):
    name = "todo"

    todo = ErrorClass(Todo, label='TODO', isfailure=False)

def contains_word(word, bytestring_):
    """
    Checks that a bytestring contains a given word. len(bytestring) should be
    a multiple of len(word).

    >>> contains_word("abcd", "abcd"*5)
    True

    >>> contains_word("ab", "ba"*5)
    False

    >>> contains_word("ab", "ab"*5+"a")
    Traceback (most recent call last):
    ...
    AssertionError: len(bytestring_) not multiple of len(word)
    """
    n = len(word)
    assert len(bytestring_)%n == 0, "len(bytestring_) not multiple of len(word)"
    chunks = [bytestring_[i:i+n] for i in xrange(0, len(bytestring_), n)]
    return word in chunks

def pixel2channels(pixel):
    alpha = (pixel >> 24) & 0xff
    red = pixel & 0xff
    green = (pixel >> 8) & 0xff
    blue = (pixel >> 16) & 0xff
    return red,green,blue,alpha

def pixel2rgba(pixel):
    return 'rgba(%s,%s,%s,%s)' % pixel2channels(pixel)

def get_unique_colors(im):
    pixels = []
    for x in range(im.width()):
        for y in range(im.height()):
            pixel = im.get_pixel(x,y)
            if pixel not in pixels:
                 pixels.append(pixel)
    pixels = sorted(pixels)
    return map(pixel2rgba,pixels)
