#!/usr/bin/python3

import os
import shutil
import logging as log
import sys
from socrate import system, conf

log.basicConfig(stream=sys.stderr, level=os.environ.get("LOG_LEVEL", "WARNING"))

conf.jinja("/default.ini", os.environ, "/data/_data_/_default_/domains/default.ini")
conf.jinja("/application.ini", os.environ, "/data/_data_/_default_/configs/application.ini")
conf.jinja("/php.ini", os.environ, "/usr/local/etc/php/conf.d/rainloop.ini")

os.execv("/usr/local/bin/apache2-foreground", ["apache2-foreground"])

