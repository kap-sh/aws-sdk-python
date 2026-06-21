"""Generated from Smithy shape ``com.amazonaws.mediaconnect#Range``."""

from typing import Literal, TypeAlias, cast

Range: TypeAlias = Literal[
    "NARROW",
    "FULL",
    "FULLPROTECT",
]


# --- restJson1 ser/de ---
def serialize_json(value: Range) -> str:
    return value


def deserialize_json(data: str) -> Range:
    return cast(Range, data)
