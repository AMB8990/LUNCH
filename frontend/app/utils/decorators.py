import os, logging
from functools import wraps
from fastapi.responses import Response
from typing import Callable, Coroutine, Any

logging.config.fileConfig('./logging.conf', disable_existing_loggers=False)
logger = logging.getLogger(__name__)

MEMBER_LIST = os.getenv('MEMBER_LIST').split(',')

def member_decorator(user:str):
    def decorator(func: Callable[..., Coroutine[Any, Any, Response]]):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            if user not in MEMBER_LIST:
                logger.warning(f"User {user} is not in member list.")
                return Response(content="Access denied", status_code=403)
            return await func(*args, **kwargs)
        return wrapper
    return decorator