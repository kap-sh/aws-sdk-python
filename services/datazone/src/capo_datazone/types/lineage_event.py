"""Generated from Smithy shape ``com.amazonaws.datazone#LineageEvent``."""

import base64
from typing import TypeAlias

LineageEvent: TypeAlias = bytes


# --- restJson1 ser/de ---
def serialize_json(value: LineageEvent) -> str:
    return base64.b64encode(value).decode("ascii")


def deserialize_json(data: str) -> LineageEvent:
    return base64.b64decode(data)
