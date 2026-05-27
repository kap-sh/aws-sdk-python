"""Generated from Smithy shape ``com.amazonaws.lambda#Blob``."""

from typing import TypeAlias
import base64

Blob: TypeAlias = bytes


# --- restJson1 ser/de ---
def serialize_json(value: Blob) -> str:
    return base64.b64encode(value).decode("ascii")


def deserialize_json(data: str) -> Blob:
    return base64.b64decode(data)
