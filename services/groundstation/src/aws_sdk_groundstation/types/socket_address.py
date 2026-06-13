"""Generated from Smithy shape ``com.amazonaws.groundstation#SocketAddress``."""

from typing import TypedDict

from aws_sdk_groundstation.errors import DeserializationError


class SocketAddress(TypedDict):
    name: "str"
    """<p>Name of a socket address.</p>"""
    port: "int"
    """<p>Port of a socket address.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SocketAddress) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["port"] = value["port"]
    return out


def deserialize_json(data: dict) -> SocketAddress:
    out: SocketAddress = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("SocketAddress.name required")
    if "port" in data:
        out["port"] = data["port"]
    else:
        raise DeserializationError("SocketAddress.port required")
    return out
