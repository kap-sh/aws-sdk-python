"""Generated from Smithy shape ``com.amazonaws.clouddirectory#BinaryAttributeValue``."""

import base64
from typing import TypeAlias

BinaryAttributeValue: TypeAlias = bytes


# --- restJson1 ser/de ---
def serialize_json(value: BinaryAttributeValue) -> str:
    return base64.b64encode(value).decode("ascii")


def deserialize_json(data: str) -> BinaryAttributeValue:
    return base64.b64decode(data)
