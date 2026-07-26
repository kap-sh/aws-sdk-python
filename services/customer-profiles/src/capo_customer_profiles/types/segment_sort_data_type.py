"""Generated from Smithy shape ``com.amazonaws.customerprofiles#SegmentSortDataType``."""

from typing import Literal, TypeAlias, cast

SegmentSortDataType: TypeAlias = Literal[
    "STRING",
    "NUMBER",
    "DATE",
]


# --- restJson1 ser/de ---
def serialize_json(value: SegmentSortDataType) -> str:
    return value


def deserialize_json(data: str) -> SegmentSortDataType:
    return cast(SegmentSortDataType, data)
