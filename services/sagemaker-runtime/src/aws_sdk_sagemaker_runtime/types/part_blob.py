"""Generated from Smithy shape ``com.amazonaws.sagemakerruntime#PartBlob``."""

import base64
from typing import TypeAlias

PartBlob: TypeAlias = bytes


# --- restJson1 ser/de ---
def serialize_json(value: PartBlob) -> str:
    return base64.b64encode(value).decode("ascii")


def deserialize_json(data: str) -> PartBlob:
    return base64.b64decode(data)
