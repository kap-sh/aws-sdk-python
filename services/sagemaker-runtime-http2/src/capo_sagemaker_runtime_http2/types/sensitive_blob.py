"""Generated from Smithy shape ``com.amazonaws.sagemakerruntimehttp2#SensitiveBlob``."""

import base64
from typing import TypeAlias

SensitiveBlob: TypeAlias = bytes


# --- restJson1 ser/de ---
def serialize_json(value: SensitiveBlob) -> str:
    return base64.b64encode(value).decode("ascii")


def deserialize_json(data: str) -> SensitiveBlob:
    return base64.b64decode(data)
