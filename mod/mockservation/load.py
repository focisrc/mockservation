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

def load(name):
    """Load data into mockservation according to extensions"""
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

    raise NameError('path "'+name+'" is invalid')
