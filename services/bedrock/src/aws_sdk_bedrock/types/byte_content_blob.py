"""Generated from Smithy shape ``com.amazonaws.bedrock#ByteContentBlob``."""

import base64
from typing import TypeAlias

ByteContentBlob: TypeAlias = bytes


# --- restJson1 ser/de ---
def serialize_json(value: ByteContentBlob) -> str:
    return base64.b64encode(value).decode("ascii")


def deserialize_json(data: str) -> ByteContentBlob:
    return base64.b64decode(data)
