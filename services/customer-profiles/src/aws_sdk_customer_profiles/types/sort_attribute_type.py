"""Generated from Smithy shape ``com.amazonaws.customerprofiles#SortAttributeType``."""

from typing import Literal, TypeAlias, cast

SortAttributeType: TypeAlias = Literal[
    "PROFILE",
    "CALCULATED",
]


# --- restJson1 ser/de ---
def serialize_json(value: SortAttributeType) -> str:
    return value


def deserialize_json(data: str) -> SortAttributeType:
    return cast(SortAttributeType, data)
