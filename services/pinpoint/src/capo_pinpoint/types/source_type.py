"""Generated from Smithy shape ``com.amazonaws.pinpoint#SourceType``."""

from typing import Literal, TypeAlias, cast

SourceType: TypeAlias = Literal[
    "ALL",
    "ANY",
    "NONE",
]


# --- restJson1 ser/de ---
def serialize_json(value: SourceType) -> str:
    return value


def deserialize_json(data: str) -> SourceType:
    return cast(SourceType, data)
