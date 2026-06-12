"""Generated from Smithy shape ``com.amazonaws.iotjobsdataplane#BinaryBlob``."""

import base64
from typing import TypeAlias

BinaryBlob: TypeAlias = bytes


# --- restJson1 ser/de ---
def serialize_json(value: BinaryBlob) -> str:
    return base64.b64encode(value).decode("ascii")


def deserialize_json(data: str) -> BinaryBlob:
    return base64.b64decode(data)
