"""Generated from Smithy shape ``com.amazonaws.customerprofiles#StringDimensionType``."""

from typing import Literal, TypeAlias, cast

StringDimensionType: TypeAlias = Literal[
    "INCLUSIVE",
    "EXCLUSIVE",
    "CONTAINS",
    "BEGINS_WITH",
    "ENDS_WITH",
]


# --- restJson1 ser/de ---
def serialize_json(value: StringDimensionType) -> str:
    return value


def deserialize_json(data: str) -> StringDimensionType:
    return cast(StringDimensionType, data)
