import pytz
import logging
from logging import getLogger, NullHandler, CRITICAL
from datetime import datetime

# 1. Preserve IST timezone export so other files in your repo don't break
IST = pytz.timezone("Asia/Kolkata")

# 2. Globally disable all log 
logging.disable(logging.CRITICAL)

# 3. Use NullHandler so nothing writes to the console or files
logging.basicConfig(
    handlers=[NullHandler()],
    level=CRITICAL
)

# 4. Explicitly silence third-party library loggers
getLogger("httpx").setLevel(CRITICAL)
getLogger("pyrogram").setLevel(CRITICAL)
getLogger("fastapi").setLevel(CRITICAL)
getLogger("uvicorn").setLevel(CRITICAL)
getLogger("uvicorn.access").setLevel(CRITICAL)
getLogger("uvicorn.error").setLevel(CRITICAL)

# 5. Export the muted LOGGER object expected by the rest of your app
LOGGER = getLogger(__name__)
LOGGER.setLevel(CRITICAL)
