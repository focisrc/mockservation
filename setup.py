#!/usr/bin/env python3
#
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

from setuptools import setup, find_packages

setup(
    name='mockservation',
    version='0.1.0',
    url='https://github.com/chanchikwan/mockservation',
    author='Chi-kwan Chan',
    author_email='chanc@email.arizona.edu',
    description='Managing, generating, and manipulating mock observations of astrophysical objects',
    packages=find_packages('mod'),
    package_dir={'': 'mod'},
    python_requires='>=3.6', # `mockservation` uses python3's f-string and typing
    install_requires=[
        'astropy>=1.3',
        'h5py>=2.6',
        'numpy>=1.12',
    ],
)
