"""Generated from Smithy shape ``com.amazonaws.iotjobsdataplane#BinaryParameterValue``."""

import base64
from typing import TypeAlias

BinaryParameterValue: TypeAlias = bytes


# --- restJson1 ser/de ---
def serialize_json(value: BinaryParameterValue) -> str:
    return base64.b64encode(value).decode("ascii")


def deserialize_json(data: str) -> BinaryParameterValue:
    return base64.b64decode(data)
