"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#PipPosition``."""

from typing import Literal, TypeAlias, cast

PipPosition: TypeAlias = Literal[
    "TOP_LEFT",
    "TOP_RIGHT",
    "BOTTOM_LEFT",
    "BOTTOM_RIGHT",
]


# --- restJson1 ser/de ---
def serialize_json(value: PipPosition) -> str:
    return value


def deserialize_json(data: str) -> PipPosition:
    return cast(PipPosition, data)
