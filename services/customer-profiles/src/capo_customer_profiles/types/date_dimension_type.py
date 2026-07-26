"""Generated from Smithy shape ``com.amazonaws.customerprofiles#DateDimensionType``."""

from typing import Literal, TypeAlias, cast

DateDimensionType: TypeAlias = Literal[
    "BEFORE",
    "AFTER",
    "BETWEEN",
    "NOT_BETWEEN",
    "ON",
]


# --- restJson1 ser/de ---
def serialize_json(value: DateDimensionType) -> str:
    return value


def deserialize_json(data: str) -> DateDimensionType:
    return cast(DateDimensionType, data)
