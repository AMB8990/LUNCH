
import os, logging
from fastapi import FastAPI

app = FastAPI()

logging.config.fileConfig('./logging.conf', disable_existing_loggers=False)
logger = logging.getLogger(__name__)

@app.get("/")
def root_page():
    logger.info("Root page are here.")
    return {"message": "HI here is root."}