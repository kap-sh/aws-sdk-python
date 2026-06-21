"""Generated from Smithy shape ``com.amazonaws.pinpoint#SegmentType``."""

from typing import Literal, TypeAlias, cast

SegmentType: TypeAlias = Literal[
    "DIMENSIONAL",
    "IMPORT",
]


# --- restJson1 ser/de ---
def serialize_json(value: SegmentType) -> str:
    return value


def deserialize_json(data: str) -> SegmentType:
    return cast(SegmentType, data)
