"""Generated from Smithy shape ``com.amazonaws.kafka#__blob``."""

import base64
from typing import TypeAlias

__blob: TypeAlias = bytes


# --- restJson1 ser/de ---
def serialize_json(value: __blob) -> str:
    return base64.b64encode(value).decode("ascii")


def deserialize_json(data: str) -> __blob:
    return base64.b64decode(data)
