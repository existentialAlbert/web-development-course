from fastapi import APIRouter

from models import Message

example_router = APIRouter()


@example_router.get("/")
def hello_world_query(msg: str = "Hello world") -> Message:
    """
    Handler function for GET /api/v1/hello_world/
    :param msg: query parameter for the endpoint
    :return: Message object created from text query parameter
    """
    return Message(text=msg)


@example_router.get("/{msg:str}")
def hello_world_path(msg: str) -> Message:
    """
    Handler function for GET /api/v1/hello_world/<text>
    :param msg: path parameter for the endpoint
    :return: Message object created from text path parameter
    """
    return Message(text=msg.replace("_", " ").capitalize())


@example_router.post("/")
def hello_world_body(msg: Message) -> Message:
    """
    Handler function for POST /api/v1/hello_world/
    :param msg: request body that looks like that: {"text": "some text"}
    :return: Message object got from request body
    """
    return msg
