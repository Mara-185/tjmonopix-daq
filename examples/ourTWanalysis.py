#!/usr/bin/env python2
"""Automated TW measurement analysis script"""
import datetime
import argparse
import logging
from tjmonopix.scans.injection_scan import InjectionScan


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input_file", help="The _scan.h5 file.")
    args = parser.parse_args()
    
    logger = logging.getLogger("main")
    logger.addHandler(logging.StreamHandler())  # Log to stderr
    logger.addHandler(logging.FileHandler("ourTWanalysis.log"))  # and also to file
    logger.info("Launched script with args %s", args)
    
    try:
        start_time = datetime.datetime.now()
        output_filename = InjectionScan.analyze(args.input_file)
        end_time = datetime.datetime.now()
        logger.info("Analysis done in %s", end_time - start_time)
        logger.info("Output file: %s", output_filename)
        logger.info("End of script")
    except:
        logger.exception("An unhandled exception occurred.")
        raise
