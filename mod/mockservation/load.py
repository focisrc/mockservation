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
        >>> img = mock.load('data_file.raw')
    """
    if os.path.isdir(name):
        load_x = load_bundle # have been implemented
    elif os.path.isfile(name):
        _, x = os.path.splitext(name)
        try:
            load_x = globals()['load_'+x.strip('.')]
        except Exception as e:
            e.args = (e.args[0]+'() is not implemented',
                      'failed to load "'+name+'"')
            raise
    else:
        raise NameError('path "'+name+'" is invalid')

    return load_x(name)

def load_bundle(name):
    """
    Load a folder as a data bundle

    Args:
        name:    Name of the data bundle

    Returns:
        A numpy array holding the loaded image(s)

    Raises:
        ImportError:    Data bundle does not provide a loader

    Examples:
        >>> import mockservation as mock
        >>> img = mock.load_bundle('data_bundle')
    """
    for loader_name in ['loader.py',
                        '.loader.py',
                        '.mockservation/loader.py']:
        full_name = name+'/'+loader_name
        if os.path.isfile(full_name):
            import importlib.util as iu
            spec   = iu.spec_from_file_location('loader', full_name)
            loader = iu.module_from_spec(spec)
            spec.loader.exec_module(loader)
            return loader.load(name)

    raise ImportError('data bundle "'+name+'" does not provide any loader')
