#!/usr/bin/python3

import os
import shutil
import logging as log
import sys
from socrate import system, conf

log.basicConfig(stream=sys.stderr, level=os.environ.get("LOG_LEVEL", "WARNING"))

os.execv("/usr/local/bin/apache2-foreground", ["apache2-foreground"])
