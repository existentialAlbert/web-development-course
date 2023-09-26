import asyncio

import uvicorn
import uvloop

from app import app
from settings import settings

config = uvicorn.Config(
    app,
    host=settings.APP_HOST,
    port=settings.APP_PORT,
    debug=settings.DEBUG,
    log_level=settings.LOGLEVEL.lower(),
)
server = uvicorn.Server(config=config)


async def main() -> None:
    """
    Entrypoint to the project. Sets up `uvloop` for increasing asyncio speed and launches `uvicorn` server.
    :return:
    """

    uvloop.install()
    await server.serve()


if __name__ == "__main__":
    asyncio.run(main())
