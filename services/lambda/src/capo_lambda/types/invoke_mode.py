"""Generated from Smithy shape ``com.amazonaws.lambda#InvokeMode``."""

from typing import Literal, TypeAlias, cast

InvokeMode: TypeAlias = Literal[
    "BUFFERED",
    "RESPONSE_STREAM",
]


# --- restJson1 ser/de ---
def serialize_json(value: InvokeMode) -> str:
    return value


def deserialize_json(data: str) -> InvokeMode:
    return cast(InvokeMode, data)
