import logging


def get_logger(name):
    log = logging.getLogger(name)
    log.setLevel(logging.DEBUG)

    sh = logging.StreamHandler()
    sh.setLevel(logging.DEBUG)
    log.addHandler(sh)

    return log
