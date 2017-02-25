# Copyright (C) 2017 Chi-kwan Chan
# Copyright (C) 2017 Steward Observatory
#
# This file is part of `mockservation`.
#
# `Mockservation` is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# `Mockservation` is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with `mockservation`.  If not, see <http://www.gnu.org/licenses/>.

import os
import sys

def load(name):
    """
    Load data into mockservation according to extensions

    Args:
        name:    Name of the data file/bundle

    Returns:
        A numpy array holding the loaded image(s)

    Raises:
        NameError:    Invalid data file/bundle name

    Examples:
        >>> import mockservation as mock
        >>> img = mock.load('gray_output.raw')
    """
    if os.path.isfile(name):
        _, x = os.path.splitext(name)
        try:
            load_x = globals()['load_'+x.strip('.')]
        except Exception as e:
            e.args = (e.args[0]+'() is not implemented',
                      'failed to load "'+name+'"')
            raise
        else:
            return load_x(name)

    if os.path.isdir(name):
        return load_bundle(name)

    raise NameError('path "'+name+'" is invalid')

def load_bundle(name):
    """
    Load a folder as a data bundle

    Args:
        name:    Name of the data bundle

    Returns:
        A numpy array holding the loaded image(s)

    Raises:
        NameError:    Invalid data bundle name

    Examples:
        >>> import mockservation as mock
        >>> img = mock.load_bundle('model_A')
    """
    path = list(sys.path) # save
    sys.path.insert(0, name)
    try:
        loader = __import__('loader')
    finally:
        sys.path[:] = path # restore

    return loader.load(name)
