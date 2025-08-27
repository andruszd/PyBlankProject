# !/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import annotations

__author__ = ""
__copyright__ = ""
__credits__ = [""]
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = ""
__email__ = ""
__status__ = "Prototype"
__description__ = ""

# IMPORTS
import argparse
import io
import json
import logging
import logging.config
import logging.handlers
import os
import pandas as pd
import datefinder



# Setup logging
def setup_logging(
        default_path='logging.json',
        default_level=logging.INFO,
        env_key='LOG_CFG'
):
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = json.load(f)
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)
    logger = logging.getLogger("auto_archive")
    return logger


# Get the arguments
def get_args():
    parser = argparse.ArgumentParser(description='Auto Archive Wazuh alerts')
    parser.add_argument('-d', '--debug', help='Debug', action='store_true')
    args = parser.parse_args()
    return args

# Main function
def main():
    logger = setup_logging()
    # Get the arguments
    args = get_args()
    debug = args.debug

    logger.info("Starting Auto Archive")
    if debug:
        logger.info("Debugging enabled")
    logger.info("All done")
    logger.info("----------------- Mark -----------------")
    exit(0)


if __name__ == '__main__':
    main()