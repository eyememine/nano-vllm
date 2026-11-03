import logging
import sys

def setup_logging():
    logging.basicConfig(
        level=logging.DEBUG,
        format="[%(levelname)-8s %(filename)s:%(lineno)d %(funcName)s] %(message)s",
        handlers=[
            logging.FileHandler("nanovllm.log", mode="w"),
            logging.StreamHandler(sys.stdout),
            
        ],
    )

logger = logging.getLogger(__name__)