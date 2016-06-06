#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# Contest Management System - http://cms-dev.github.io/
# Copyright © 2011-2016 Luca Wehrstedt <luca.wehrstedt@gmail.com>
# Copyright © 2016 William Di Luigi <williamdiluigi@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

import argparse
import io
try:
    import json5 as json
except ImportError:
    import json
import logging
import os
import six
import sys

from cmsranking.Logger import add_file_handler


logger = logging.getLogger(__name__)


def utf8_decoder(value):
    """Decode given binary to text (if it isn't already) using UTF8.

    value (string): value to decode.

    return (unicode): decoded value.

    raise (TypeError): if value isn't a string.

    """
    if isinstance(value, six.text_type):
        return value
    elif isinstance(value, six.binary_type):
        return value.decode('utf-8')
    else:
        raise TypeError("Not a string.")


class Config(object):
    """An object holding the current configuration.

    """
    def __init__(self):
        """Fill this object with the default values for each key.

        """
        parser = argparse.ArgumentParser(
            description="Ranking Web Server.")

        parser.add_argument(
            "-d", "--drop",
            action="store_true",
            help="Drop the data already stored.")

        parser.add_argument(
            "-p", "--http-port", default=8890,
            action="store", type=int,
            help="Listening HTTP port for RankingWebServer.")

        parser.add_argument(
            "--https-port",
            action="store", type=int,
            help="Listening HTTPS port for RankingWebServer.")

        parser.add_argument(
            "--https-certfile",
            action="store", type=utf8_decoder,
            help="HTTPS certificate file for RankingWebServer.")

        parser.add_argument(
            "--https-keyfile",
            action="store", type=utf8_decoder,
            help="HTTPS key file for RankingWebServer.")

        parser.add_argument(
            "-t", "--timeout", default=600,  # 10 minutes (in seconds)
            action="store", type=int,
            help="Listening HTTPS port for RankingWebServer.")

        parser.add_argument(
            "-b", "--bind-address", default="",
            action="store", type=utf8_decoder,
            help="Listening address for RankingWebServer.")

        parser.add_argument(
            "--realm-name", default="Scoreboard",
            action="store", type=utf8_decoder,
            help="Realm name for authentication.")

        parser.add_argument(
            "-l", "--login", default="usern4me:passw0rd",
            action="store", type=utf8_decoder,
            help="Login information for adding and editing data.")

        parser.add_argument(
            "--buffer-size", default=100,  # Needs to be strictly positive
            action="store", type=int,
            help="Listening HTTPS port for RankingWebServer.")

        parser.add_argument(
            "-c", "--config",
            action="store", type=utf8_decoder,
            help="Path to a JSON config file.")

        parser.add_argument(
            "--log-dir", default=os.path.join("/", "var", "local", "log",
                                              "cms", "ranking"),
            action="store", type=utf8_decoder,
            help="Directory where RWS will store log files.")

        parser.add_argument(
            "--lib-dir", default=os.path.join("/", "var", "local", "lib",
                                              "cms", "ranking"),
            action="store", type=utf8_decoder,
            help="Directory where RWS will store runtime data.")

        self.args = parser.parse_args()

        # Ensure that lib and log directories exist (Python >= 3.2)
        #os.makedirs(self.args.lib_dir, exists_ok=True)
        #os.makedirs(self.args.log_dir, exists_ok=True)

        # Ensure that lib and log directories exist (Python < 3.2)
        try:
            os.makedirs(self.args.lib_dir)
        except OSError:
            pass  # We assume the directory already exists...
        try:
            os.makedirs(self.args.log_dir)
        except OSError:
            pass  # We assume the directory already exists...

        # Send log output to log_dir
        add_file_handler(self.args.log_dir)

        # Parse the authentication string into username and password
        try:
            self.username, self.password = self.args.login.split(":")
        except ValueError:
            logger.exception("The login string should follow the "
                "username:password format.")
            sys.exit(1)

        # Read (and override) options from a config file, if specified
        if self.args.config:
            self.load(self.args.config)

    def get(self, key):
        """Get the config value for the given key.

        """
        return getattr(self.args, key)

    def load(self, path):
        """Populate the Config class with everything that sits inside
        the given JSON file path

        path (string): the path of the JSON config file.

        """
        try:
            with io.open(path, 'rb') as fobj:
                data = json.load(fobj)

                # Put everything.
                for key, value in data.iteritems():
                    setattr(self.args, key, value)
        except IOError:
            logger.exception("Error opening config file.")
        except ValueError:
            logger.exception("Config file is invalid JSON.")
        else:
            logger.info("Using config file %s.", path)


# Create an instance of the Config class.
config = Config()
