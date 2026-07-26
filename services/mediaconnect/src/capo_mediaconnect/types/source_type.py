"""Generated from Smithy shape ``com.amazonaws.mediaconnect#SourceType``."""

from typing import Literal, TypeAlias, cast

SourceType: TypeAlias = Literal[
    "OWNED",
    "ENTITLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: SourceType) -> str:
    return value


def deserialize_json(data: str) -> SourceType:
    return cast(SourceType, data)
