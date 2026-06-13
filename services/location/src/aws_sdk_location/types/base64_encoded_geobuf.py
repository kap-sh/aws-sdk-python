"""Generated from Smithy shape ``com.amazonaws.location#Base64EncodedGeobuf``."""

import base64
from typing import TypeAlias

Base64EncodedGeobuf: TypeAlias = bytes


# --- restJson1 ser/de ---
def serialize_json(value: Base64EncodedGeobuf) -> str:
    return base64.b64encode(value).decode("ascii")


def deserialize_json(data: str) -> Base64EncodedGeobuf:
    return base64.b64decode(data)
