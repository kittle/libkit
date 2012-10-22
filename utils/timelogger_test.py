import time

from timelogger import timelogger


def test():
    import logging
    logging.basicConfig()
    logger = logging.getLogger()

    with timelogger(None, logger.info, "Zzzzzz") as z:
        time.sleep(1)
        a = 1
    assert a == 1
    assert z.duration > 1


if __name__ == "__main__":
    test()