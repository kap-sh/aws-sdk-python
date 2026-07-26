"""Generated from Smithy shape ``com.amazonaws.iotsitewise#RawValueType``."""

from typing import Literal, TypeAlias, cast

RawValueType: TypeAlias = Literal[
    "D",
    "B",
    "S",
    "I",
    "U",
]


# --- restJson1 ser/de ---
def serialize_json(value: RawValueType) -> str:
    return value


def deserialize_json(data: str) -> RawValueType:
    return cast(RawValueType, data)
