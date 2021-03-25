import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger()
logger.addHandler(logging.FileHandler("Fib.log"))


def fib(n):

    if n < 3:
        return 1
    return fib(n-1)+fib(n-2)

logger.info(fib(20))
