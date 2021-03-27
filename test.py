#!/usr/bin/env python
import logging
import sys

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO,
                    stream=sys.stdout,
                    format='%(message)s')


def main():
    logger.info("Kill me!!!")
    for x in ["Lalall", "Hello!"]:
        logger.info(x)


if __name__ == "__main__":
    main()
