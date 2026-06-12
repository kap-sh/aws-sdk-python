"""Generated from Smithy shape ``com.amazonaws.iot#BinaryCommandExecutionResult``."""

import base64
from typing import TypeAlias

BinaryCommandExecutionResult: TypeAlias = bytes


# --- restJson1 ser/de ---
def serialize_json(value: BinaryCommandExecutionResult) -> str:
    return base64.b64encode(value).decode("ascii")


def deserialize_json(data: str) -> BinaryCommandExecutionResult:
    return base64.b64decode(data)
