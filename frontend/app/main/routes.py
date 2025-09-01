import os, logging
from flask import current_app, send_from_directory, make_response, redirect, url_for
from app.main import main_bp
from app.utils.decorators import member_decorator

logging.config.fileConfig('./logging.conf', disable_existing_loggers=False)
logger = logging.getLogger(__name__)

@main_bp.route("/main")
@member_decorator
def react():
    react_path=current_app.config['REACT_PATH']
    logger.info(f"React path is {react_path}")
    return send_from_directory(react_path, 'index.html')