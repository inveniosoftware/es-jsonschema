# -*- coding: utf-8 -*-
#
# This file is part of es-jsonschema.
# Copyright (C) 2015 CERN.
#
# es-jsonschema is free software; you can redistribute it
# and/or modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.
#
# es-jsonschema is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with es-jsonschema; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston,
# MA 02111-1307, USA.
#
# In applying this license, CERN does not
# waive the privileges and immunities granted to it by virtue of its status
# as an Intergovernmental Organization or submit itself to any jurisdiction.

"""Exceptions used in this package."""


class JsonSchemaSupportError(Exception):
    """Exception thrown when a json schema is not supported by a function."""

    def __init__(self, message, path, *args, **kwargs):
        """Constructor.

        :param message: error message
        :param path: path of the failing file
        """
        super(JsonSchemaSupportError, self).__init__(*args, **kwargs)
        self.message = message
        self.path = path

    def __str__(self):
        """Return the formatted error message string."""
        return 'ERROR {0} IN {1}'.format(self.message, self.path)
