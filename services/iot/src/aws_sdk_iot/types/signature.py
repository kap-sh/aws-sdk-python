"""Generated from Smithy shape ``com.amazonaws.iot#Signature``."""

import base64
from typing import TypeAlias

Signature: TypeAlias = bytes


# --- restJson1 ser/de ---
def serialize_json(value: Signature) -> str:
    return base64.b64encode(value).decode("ascii")


def deserialize_json(data: str) -> Signature:
    return base64.b64decode(data)
