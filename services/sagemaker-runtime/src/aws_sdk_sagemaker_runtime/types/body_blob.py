"""Generated from Smithy shape ``com.amazonaws.sagemakerruntime#BodyBlob``."""

import base64
from typing import TypeAlias

BodyBlob: TypeAlias = bytes


# --- restJson1 ser/de ---
def serialize_json(value: BodyBlob) -> str:
    return base64.b64encode(value).decode("ascii")


def deserialize_json(data: str) -> BodyBlob:
    return base64.b64decode(data)
