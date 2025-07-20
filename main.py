import logging
from rich.logging import RichHandler

# Configure RichHandler with custom options
logging.basicConfig(
    level=logging.DEBUG,  # Show all levels
    format="%(filename)s %(levelname)s | %(asctime)s | %(message)s",
    handlers=[RichHandler(rich_tracebacks=True)]
)

logger = logging.getLogger()

logger.debug("This is a debug message: invisible unless level is DEBUG.")
logger.info("App started successfully.")
logger.warning("Deprecated function is used here.")
logger.error("An error occurred during processing.")
logger.critical("Critical failure! Application will terminate.")