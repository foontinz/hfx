import argparse
import click
import aiofiles

from typing import Annotated
from litestar import Litestar, get, post, MediaType
from litestar.logging import LoggingConfig
from litestar.plugins import CLIPlugin
from litestar.datastructures import UploadFile 
from litestar.enums import RequestEncodingType
from litestar.params import Body
from pathlib import Path


logging_config = LoggingConfig(
    root={"level": "INFO", "handlers": ["queue_listener"]},
    formatters={
        "standard": {"format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"}
    },
    log_exceptions="always",
)

@get("/")
async def index() -> str:
    return "To send a file use: `curl -X POST -F 'file=@/path/to/yourfile.txt' http://this-server-ip.com/upload`"

@post(path="/upload")
async def upload_file(
        data: Annotated[UploadFile, Body(media_type=RequestEncodingType.MULTI_PART)],
        ) -> str:
    content = await data.read()
    filename = data.filename
    async with aiofiles.open(FILES_OUTPUT / filename, "wb") as f:
        await f.write(content)

    return "Upload successful"

FILES_OUTPUT = Path("uploads")
FILES_OUTPUT.mkdir(exist_ok=True)
app = Litestar(route_handlers=[index, upload_file], logging_config=logging_config)
