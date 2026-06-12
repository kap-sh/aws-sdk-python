"""Generated from Smithy shape ``com.amazonaws.iotdataplane#JsonDocument``."""

import base64
from typing import TypeAlias

JsonDocument: TypeAlias = bytes


# --- restJson1 ser/de ---
def serialize_json(value: JsonDocument) -> str:
    return base64.b64encode(value).decode("ascii")


def deserialize_json(data: str) -> JsonDocument:
    return base64.b64decode(data)
