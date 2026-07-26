"""Generated from Smithy shape ``com.amazonaws.lambda#Blob``."""

import base64
from typing import TypeAlias

Blob: TypeAlias = bytes


# --- restJson1 ser/de ---
def serialize_json(value: Blob) -> str:
    return base64.b64encode(value).decode("ascii")


def deserialize_json(data: str) -> Blob:
    return base64.b64decode(data)
