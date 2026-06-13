"""Generated from Smithy shape ``com.amazonaws.mediaconnect#RouterOutputMessage``."""

from typing import TypedDict

from aws_sdk_mediaconnect.errors import DeserializationError


class RouterOutputMessage(TypedDict):
    code: "str"
    """<p>The code associated with the router output message.</p>"""
    message: "str"
    """<p>The message text associated with the router output message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouterOutputMessage) -> dict:
    out: dict = {}
    out["code"] = value["code"]
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> RouterOutputMessage:
    out: RouterOutputMessage = {}  # type: ignore[typeddict-item]
    if "code" in data:
        out["code"] = data["code"]
    else:
        raise DeserializationError("RouterOutputMessage.code required")
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("RouterOutputMessage.message required")
    return out
