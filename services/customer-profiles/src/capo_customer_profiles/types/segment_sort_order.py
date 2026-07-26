"""Generated from Smithy shape ``com.amazonaws.customerprofiles#SegmentSortOrder``."""

from typing import Literal, TypeAlias, cast

SegmentSortOrder: TypeAlias = Literal[
    "ASC",
    "DESC",
]


# --- restJson1 ser/de ---
def serialize_json(value: SegmentSortOrder) -> str:
    return value


def deserialize_json(data: str) -> SegmentSortOrder:
    return cast(SegmentSortOrder, data)
