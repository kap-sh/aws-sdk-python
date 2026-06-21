"""Generated from Smithy shape ``com.amazonaws.lexruntimev2#InputMode``."""

from typing import Literal, TypeAlias, cast

InputMode: TypeAlias = Literal[
    "Text",
    "Speech",
    "DTMF",
]


# --- restJson1 ser/de ---
def serialize_json(value: InputMode) -> str:
    return value


def deserialize_json(data: str) -> InputMode:
    return cast(InputMode, data)
