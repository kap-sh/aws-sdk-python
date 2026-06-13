"""Generated from Smithy shape ``com.amazonaws.mediaconnect#RouterInputMessage``."""

from typing import TypedDict

from aws_sdk_mediaconnect.errors import DeserializationError


class RouterInputMessage(TypedDict):
    code: "str"
    """<p>The code associated with the router input message.</p>"""
    message: "str"
    """<p>The message text associated with the router input message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouterInputMessage) -> dict:
    out: dict = {}
    out["code"] = value["code"]
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> RouterInputMessage:
    out: RouterInputMessage = {}  # type: ignore[typeddict-item]
    if "code" in data:
        out["code"] = data["code"]
    else:
        raise DeserializationError("RouterInputMessage.code required")
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("RouterInputMessage.message required")
    return out
