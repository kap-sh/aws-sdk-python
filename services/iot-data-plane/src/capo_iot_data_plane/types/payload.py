"""Generated from Smithy shape ``com.amazonaws.iotdataplane#Payload``."""

import base64
from typing import TypeAlias

Payload: TypeAlias = bytes


# --- restJson1 ser/de ---
def serialize_json(value: Payload) -> str:
    return base64.b64encode(value).decode("ascii")


def deserialize_json(data: str) -> Payload:
    return base64.b64decode(data)
