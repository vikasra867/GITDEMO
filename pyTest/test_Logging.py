import logging


# FileHandler
# formattor
# path
# file
#
def test_loggingDemo():
    logger = logging.getLogger(__name__)
    fileHandler = logging.FileHandler('logFile.log')

    formatter = logging.Formatter("%(asctime)s, :%(levelname)s, : %(name)s : %(message)s")
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)
    logger.setLevel(logging.INFO)

    logger.debug("I am debugger information")
    logger.info("I am Information only")
    logger.warning("warning")
    logger.error("Error")
    logger.critical("Critical")

