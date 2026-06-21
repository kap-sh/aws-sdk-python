"""Generated from Smithy shape ``com.amazonaws.customerprofiles#SegmentType``."""

from typing import Literal, TypeAlias, cast

SegmentType: TypeAlias = Literal[
    "CLASSIC",
    "ENHANCED",
]


# --- restJson1 ser/de ---
def serialize_json(value: SegmentType) -> str:
    return value


def deserialize_json(data: str) -> SegmentType:
    return cast(SegmentType, data)
