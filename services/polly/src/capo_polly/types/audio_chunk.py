"""Generated from Smithy shape ``com.amazonaws.polly#AudioChunk``."""

import base64
from typing import TypeAlias

AudioChunk: TypeAlias = bytes


# --- restJson1 ser/de ---
def serialize_json(value: AudioChunk) -> str:
    return base64.b64encode(value).decode("ascii")


def deserialize_json(data: str) -> AudioChunk:
    return base64.b64decode(data)
