"""Generated from Smithy shape ``com.amazonaws.lambda#BinaryOperationPayload``."""

import base64
from typing import TypeAlias

BinaryOperationPayload: TypeAlias = bytes


# --- restJson1 ser/de ---
def serialize_json(value: BinaryOperationPayload) -> str:
    return base64.b64encode(value).decode("ascii")


def deserialize_json(data: str) -> BinaryOperationPayload:
    return base64.b64decode(data)
